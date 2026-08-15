#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_opcode_semantics.py — сборка артефактов этапа 15.10.

Семантика опкодов восстановлена СТАТИЧЕСКИ из первичного кода:
  - исполнитель действий: g.H() (g.java:17353) — switch 110..172
  - исполнитель условий: g.K() (g.java:17740) — switch 150..172
  - skip/if-else: g.n(boolean) (g.java:17290) — 145/146 (скобки), 143 (else), 144 (endif)
  - вход в скрипт: g.b(int) (g.java:17268): bP=n, bO=H[n], bQ=A[n] -> H()
  - диалоговый режим: g.J() (g.java:17722) / g.I() (g.java:17717) — цикл до 159
  - методы-действия прочитаны в телах (см. evidence line)

Вывод:
  research/analysis/v2/script-engine/dispatch-trace.json
  research/analysis/v2/script-engine/opcode-samples/opcode-XXX.json
  research/analysis/v2/script-engine/opcode-master-v2.json
  research/analysis/v2/missions/mission-script-flow-v2.md
"""
import json
import sys
from collections import Counter
from pathlib import Path

MISS = Path("research/analysis/v2/missions")
SE = Path("research/analysis/v2/script-engine")

# ---------------------------------------------------------------- семантика
# (opcode, имя, класс, reads, writes, calls, описание, evidence)
SEM = [
    (110, "entity_command", "ENTITY", "z[o+0..16]", "сущность: g[28],g[29], позиция, направление",
     "g.c(n,n2,n3,n4); f.a(f2,n7,n8,mask,n12,n11); f2.a.a(n5,n6)",
     "Команда сущности: поиск по (n,n2,n3,n4); направление n8->бит-маска (0/1/7=8256, 4/3/5=4112, 2=1028, 6=2304); действие n7; позиция (n5,n6).",
     "g.java:18083 a(int x8)"),
    (111, "teleport_player", "ENTITY", "z[o+0], z[o+2]", "g.c.a (позиция игрока)",
     "g.c.a.b(n4,n3); g.a(c,1,bt)",
     "Телепорт игрока относительно объекта d: n=0: x+=n2*16,y-=16; n=1: x+=n2*16 (+y=g[3] если d.L==11); n=2: x-=16; n=3: x+=g[2]*16.",
     "g.java:18136 n(int,int)"),
    (112, "object_action", "OBJECT", "z[o+0],z[o+4],z[o+6],z[o+8],z[o+14]", "объект-тайл g.c(2,...)",
     "g.b(n,n2,n3,n4,var4_4)",
     "Действие над объектом-тайлом: bl=true -> f.h+f.c(f2,4)+f.m (деактивация); bl=false -> проверка проходимости f.s + маркировка g[n6+14].",
     "g.java:18823 b(int,int,int,int,boolean)"),
    (113, "tile_object_field_write", "TILE", "z[o+2],z[o+4],z[o+6],z[o+12]", "g.g[layer][x][y].g[prop]",
     "g.j(n,n2,n3,n4)",
     "Запись поля объекта-тайла: L25->g[9], L20->g[6], L21->g[4], L22->g[6], L24->g[2].",
     "g.java:18203 j(int,int,int,int)"),
    (114, "tile_object_command", "TILE", "z[o+2],z[o+4],z[o+6],z[o+8]", "g.g[n][n2][n3].g[0]",
     "g.k(n,n2,n3,n4)",
     "Команда объекту-тайлу: g[0]=n4; L21->f.b; L23 (дверь)->f.a(открыть/закрыть); L25->f.a.",
     "g.java:18239 k(int,int,int,int)"),
    (115, "entity_prop_write", "ENTITY", "z[o+2],z[o+4],z[o+6],z[o+8],z[o+10]", "f[layer][x][y].g[n4]",
     "g.d(n,n2,n3,n4,n5)",
     "Запись свойства сущности сетки: g[n4] = n5.",
     "g.java:18262 d(int,int,int,int,int)"),
    (116, "entity_prop_add", "ENTITY", "z[o+2],z[o+4],z[o+6],z[o+8],z[o+10]", "g.f[layer][x][y].g[n4]",
     "g.e(n,n2,n3,n4,n5)",
     "Инкремент свойства сущности сетки: g[n4] += n5.",
     "g.java:18272 e(int,int,int,int,int)"),
    (117, "wait_until", "CONTROL", "z[o+0]", "пауза исполнения",
     "g.d(...); цикл g.Q()/g.e(...)",
     "Ожидание: если var4_4 (P||a==2) -> пропуск; иначе цикл Q() пока e(...)!=0 — блокирующее ожидание условия.",
     "g.java:17400 case 117"),
    (118, "place_entity_at_tile", "ENTITY", "z[o+0],z[o+4],z[o+6],z[o+8],z[o+10],z[o+12]",
     "сущность var8_8: позиция a.b(x*16+8, y*16+8); g[9..12] для L14",
     "g.c(var0,var1,var2,var3); g.d(var8_8); g.a(var8_8,1,true); g.c(var8_8)",
     "Размещение сущности в тайле: поиск; удаление если L 9/10/11/16; флаг 1 для L 3/1/0; позиция = центр тайла (x*16+8, y*16+8); обработка дверей L23; L14 -> g[9..12]=AABB.",
     "g.java:18302 c(int x6)"),
    (119, "delayed_call", "CONTROL", "z[o+0..18]", "m (флаг), g.i(n7,n8)",
     "g.c(n,n2,n3,n4); g.d(f2,n5) или g.p(f2); g.i(n7,n8)",
     "Отложенный вызов: если n5 >= delta -> g.d(f2,n5) (задержка), иначе g.p(f2) (немедленно); n6==1 -> g.i(n7,n8); m = (n9==1).",
     "g.java:18287 a(int x9)"),
    (120, "prop14_write", "ENTITY", "z[o+0],z[o+2]", "f2.g[n3+14]",
     "g.p(n,n2)",
     "Запись байта n2 в свойство 14 (палитра/флаг) сущности g.a(n): g[n3+14] merge 65280.",
     "g.java:18302 p(int,int)"),
    (121, "anim_stack_switch", "ANIMATION", "-", "f/g стеки, ch/ci/cm/cn, co, A[]",
     "g.cp(); g.bh()",
     "Переключение стека анимаций/отложенных действий (cp) + сброс массива A (bh: A[1]=-1,A[0]=0,A[7]=0).",
     "g.java:20678 cp(), 12199 bh()"),
    (122, "noop", "CONTROL", "-", "-", "-", "Нет операции (break).", "g.java:17444 case 122"),
    (123, "subroutine_call", "CONTROL", "z[o+4]", "bP, bO, bQ (указатель скрипта)",
     "g.bW(); bP=z[o+4]; bO=H[idx]; bQ=A[idx]",
     "Вызов субскрипта: переключение исполнения на скрипт-тайл с индексом z[o+4] (H/A таблицы).",
     "g.java:17528-17537 (var3_3 = var0==123)"),
    (124, "condition_prop_cmp", "CONTROL", "z[o+0..14]", "var5_5 (результат условия)",
     "g.c(2, o+10, o+12, o+14, o+0, o+2, o+4, o+6)",
     "УСЛОВИЕ: сравнение свойства сущности: f2 = g.c(n,n2,n3,n4); n9=f2.g[n5]; switch(n6): 0==,1!=,2<,3>,4<=,5>=... (n7) — результат для ветвления if/else (145/146).",
     "g.java:18460 c(int x8)"),
    (125, "condition_special", "CONTROL", "z[o+0..6]", "var5_5",
     "g.c(1,0,0,0,o+0,o+2,o+4,o+6)",
     "УСЛОВИЕ (вариант с фикс. сущностью 1): сравнение свойств.",
     "g.java:18460 c(int x8)"),
    (126, "add_score_money", "PROGRESSION", "z[o+0]", "g.L[4]",
     "g.ah(n)",
     "Добавление очков/денег: L[4] += 45000*n/100, cap 45000.",
     "g.java:21532 ah(int)"),
    (127, "entity_command_ptr", "ENTITY", "z[o+0..8], z[o+22], z[o+24]", "сущность; указатель на z",
     "g.a(o+0,o+2,o+4,o+6,o+8,o+22,o+24, var1_1+10, g.z)",
     "Команда сущности с передачей указателя на буфер данных (var1_1+10) — расширенная команда.",
     "g.java:17502 case 127"),
    (128, "player_prop_write", "ENTITY", "z[o+0],z[o+2]", "g.c.g[n]",
     "g.o(n,n2)",
     "Установка поля игрока: g.c.g[n] = n2; n==1 -> g.e(c) (пересчёт).",
     "g.java:18280 o(int,int)"),
    (129, "noop", "CONTROL", "-", "-", "-", "Нет операции.", "g.java:17462 case 129"),
    (130, "entity_move", "ENTITY", "z[o+0..12]", "сущность f2: перемещение",
     "g.c(n,n2,n3,n4); g.b(f2,n2,n3,n5,n6,bl)",
     "Перемещение сущности: поиск; L21 -> пропуск; иначе g.b(f2,...,bl) (перемещение); null -> g.U(n5) или g.bh().",
     "g.java:18419 a(int x7,boolean)"),
    (131, "set_bD", "STATE", "z[o+0]", "g.bD",
     "g.bD = z[o+0]",
     "Установка глобальной переменной миссии bD (используется в header/загрузке).",
     "g.java:17470 case 131"),
    (132, "reset_dialog_hp", "STATE", "-", "g.d.g[9]",
     "if (g.d != null) g.d.g[9] = 0",
     "Сброс свойства 9 диалогового объекта d (HP?) в 0.",
     "g.java:17474 case 132"),
    (133, "remove_sprites", "GRAPHICS", "z[o+0]", "b[n] (набор спрайтов)",
     "g.s(n)",
     "Удаление набора спрайтов n: цикл g.r(n2+i) для b[n] элементов.",
     "g.java:2147 s(int)"),
    (134, "switch_character", "ENTITY", "z[o+0],z[o+2],z[o+4]", "активный персонаж (c[], bt, j)",
     "g.a(n,n2,n3,bl)",
     "Переключение активного персонажа: n2==1 -> j=true; n<0 -> al(); g.a(n,n4) — выбор.",
     "g.java:18549 a(int,int,int,boolean)"),
    (135, "entity_action3", "ENTITY", "z[o+0],z[o+2]", "сущность",
     "g.e(n,n2,bl)",
     "Действие над сущностью (3 аргумента + bool).",
     "g.java:17484 case 135"),
    (136, "entity_command_ptr2", "ENTITY", "z[o+0..14]", "g.co (указатель), сущность",
     "g.co = var1_1+14; g.a(o+0,o+4,o+6,o+8,o+10,o+12,o+14,false)",
     "Команда сущности с сохранением указателя в g.co.",
     "g.java:17424 case 136"),
    (137, "effect_start", "GRAPHICS", "z[o+0],z[o+2],z[o+4],z[o+6]", "g.E[] (эффект)",
     "g.i(n,n2,n3,n4) или g.bz()",
     "Запуск полноэкранного эффекта E: E[0]=3, E[2]=n+1, E[3]=n2, E[6]=n3, E[7]=n4; в P-режиме сброс E[0]=-1 (bz).",
     "g.java:13554 i(int x4), 13550 bz()"),
    (138, "value_compute", "CONTROL", "z[o+0]", "var5_5 (результат)",
     "g.r(n)",
     "Вычисление: var5_5 = c[w][4] - (n>>1) — значение в регистр.",
     "g.java:3080 r(int)"),
    (139, "set_bi", "STATE", "z[o+0]", "g.bi",
     "g.bi = z[o+0]",
     "Установка переменной bi.",
     "g.java:17494 case 139"),
    (140, "noop", "CONTROL", "-", "-", "-", "Нет операции.", "g.java:17496 case 140"),
    (141, "switch_character_full", "ENTITY", "z[o+0]", "активный персонаж c[], bt, оружие L[1], слой",
     "g.d(n,false)",
     "Полная смена активного персонажа: поиск по g[4]==n; c=c[n2], bt=n2; сброс f.a=0, L[1]=-1, M[0]=-1; перезагрузка оружия g.af/g.ai; смена слоя g.m если нужно.",
     "g.java:14794 d(int,boolean)"),
    (142, "teleport_character", "ENTITY", "z[o+0..14]", "персонаж: g[26],g[27], позиция a.b(n5,n6)",
     "g.a(n,n2,n3,n4,n5,n6,n7)",
     "Телепорт персонажа: поиск по g[4]==n; g[26]=n2, g[27]=n3 (слой); позиция (n5,n6); смена слоя g.m для игрока; f.d(c,0).",
     "g.java:14727 a(int x7)"),
    (143, "else_marker", "CONTROL", "-", "-", "-",
     "Маркер else: в g.n(boolean) проверки n2==143 — граница then/else блока.",
     "g.java:17303-17340 n(boolean)"),
    (144, "endif_marker", "CONTROL", "-", "-", "-",
     "Маркер endif: в g.n(boolean) проверки n2==144 — конец if-блока.",
     "g.java:17303-17340 n(boolean)"),
    (145, "if_open", "CONTROL", "-", "баланс скобок n5",
     "g.n(bl): n4==145 -> --n5",
     "Открывающая скобка if: балансируется с 146; пропускается до 146 при ложном условии (K() вернула false).",
     "g.java:17312-17340 n(boolean)"),
    (146, "if_close", "CONTROL", "-", "баланс скобок n5",
     "g.n(bl): n4==146 -> --n5; если n5==0 -> return",
     "Закрывающая скобка if/else.",
     "g.java:17312-17340 n(boolean)"),
    (147, "entity_command_result", "ENTITY", "z[o+0..10]", "сущность по результату g.c(...)",
     "g.a(g.c(o+0,o+4,o+6,o+8), o+10, g.z, o+12)",
     "Команда сущности, выбранной по 4 координатам, с передачей z-буфера и указателя.",
     "g.java:17504 case 147"),
    (148, "set_npc_target", "ENTITY", "z[o+0..22]", "цель NPC (f.c/f.a между f2 и f3)",
     "g.a(10 args): f.c(f2,f3) или f.a(f2,f3,n10!=0)",
     "SetNPCTarget: выбор двух сущностей (MC/NPC); n9==0 -> f.c (связь), иначе f.a (цель/сопровождение).",
     "g.java:18393 a(int x10)"),
    (150, "entity_command_var", "ENTITY", "z[o+0..16]", "сущность; var8_8 = (o+12==1?0:-1)",
     "g.a(o+0,o+4,o+6,o+8,o+10,var8_8,o+14,o+16)",
     "Команда сущности (вариант 110) с параметром var8_8, зависящим от z[o+12].",
     "g.java:17566 case 150"),
    (151, "spawn_entity", "ENTITY", "z[o+0..22]", "новая сущность; g.ay, g.r, g.u",
     "g.aS(); g.g(0,var10_14,var11_15); g.a(g.b,0,var8_9,var9_12,null,a[7],var10_14)",
     "СПАВН сущности: var8_9=тип?; var9_12=y (если <0 -> g.d.g[3]); var10_14=x (-1->g.c.g[4], -2->g.d.g[4], -3->-1); g.ay=o+8; g.r=(o+10==1); g.u=(o+18==1); создание через g.a(g.b,0,...).",
     "g.java:17572-17603 case 151"),
    (152, "entity_command_ptr3", "ENTITY", "z[o+0..10]", "сущность; f.y",
     "g.f(var7_7, o+2, o+4, o+10, var1_1)",
     "Команда сущности с передачей указателя var1_1 (метод g.f — перегрузка; var7_7 = o+0 или f.y).",
     "g.java:17604 case 152"),
    (153, "timer_reset", "CONTROL", "-", "g.bV",
     "g.cb()",
     "Сброс таймера bV=0 (используется a(n,bl): 'если прошло n мс').",
     "g.java:18754 cb()"),
    (154, "entity_action1", "ENTITY", "z[o+0]", "сущность",
     "g.d(o+0) (+ в K(): g.Q(), g.e(...))",
     "Действие над сущностью (1 аргумент); в K()-режиме — проверка.",
     "g.java:17610 case 154"),
    (155, "delayed_call2", "CONTROL", "z[o+0..18]", "m; g.i(n7,n8)",
     "g.a(9 args)",
     "Отложенный вызов (как 119).",
     "g.java:17612 case 155"),
    (156, "camera_scroll_y", "CAMERA", "z[o+2]", "g.aL (вертикальный скролл), g.g(4,...)",
     "g.R(n)",
     "Вертикальный скролл камеры: aL += n (с коррекцией -30%), кламп [0,200].",
     "g.java:11361 R(int)"),
    (157, "dialog_state_change", "STATE", "z[o+0..8]", "g.u, g.v, g.b[0], состояние",
     "g.b[0].a(0); g.u=false; g.a(0,o+0,o+2,o+4==1,o+6==1); g.v=o+8==1",
     "Смена состояния/диалога: сброс u; вызов g.a(0, ...) с параметрами; установка v.",
     "g.java:17617-17622 case 157"),
    (158, "set_Q_flag", "STATE", "z[o+0],z[o+2],z[o+4]", "g.Q, g.j(n,n2)",
     "g.Q = (o+4==1); g.j(o+0, o+2)",
     "Установка флага Q (пауза скрипта) + вызов j.",
     "g.java:17624 case 158"),
    (159, "script_end", "CONTROL", "-", "P (диалог-режим)",
     "g.x() (условие конца); P=false",
     "ТЕРМИНАТОР скрипта: J()/I() цикл выполняется пока n != 159; в K(): g.x() проверка конца.",
     "g.java:17791 case 159"),
    (160, "spawn_entity2", "ENTITY", "z[o+0..14]", "новая сущность; g.ay=0",
     "g.aS(); g.a(0,g.c); g.a(0,o+0,-3,-3,a[7]); g.a(g.b,0,o+2,o+4,null,a[7],var8_11,o+12,o+14,var1_1)",
     "СПАВН сущности (вариант 151): var8_11 = o+0 (-1/-2/-3 -> g.c.g[4]/g.d.g[4]/-1); позиция (o+2,o+4).",
     "g.java:17628-17646 case 160"),
    (161, "capture_dialog_state", "STATE", "-", "g.dE, g.O",
     "g.dE = (g.d!=null && g.d.L==11 ? g.d.g[12] : -3); g.O=true",
     "Захват состояния диалогового объекта d (g[12]) в dE; установка флага O.",
     "g.java:17648-17653 case 161"),
    (162, "entity_command_bool", "ENTITY", "z[o+0..16]", "сущность; g.co=-1",
     "g.a(o+0,o+4,o+6,o+8,o+10,o+12,o+14, o+16==1)",
     "Команда сущности с bool-флагом (o+16==1); сброс co=-1.",
     "g.java:17655-17658 case 162"),
    (165, "transition_to_gameplay", "STATE", "z[o+0]", "g.aX; экран e(0,38,0,38); state",
     "g.T(n)",
     "Переход: aX=n; затемнение e(0,38,0,38); n==3 -> g.a(6,-1) — выход в геймплей (state 6).",
     "g.java:11703 T(int)"),
    (167, "object_activate", "OBJECT", "z[o+0],z[o+2],z[o+4],z[o+6]", "g.X(-1); объект",
     "g.a(n,n2,n3,n4,bl)",
     "Активация объекта: сброс X(-1); если n3==0 && n2!=1 && !bl -> g.a(n,false,n4).",
     "g.java:18765 a(int,int,int,int,boolean)"),
    (168, "camera_target", "CAMERA", "z[o+0..8]", "g.B[1..5], g.B[0]=2, g.G",
     "g.g(n,n2,n3,n4); g.G = (o+8==1)",
     "Установка цели движения камеры/сцены: B[1..4]=параметры; B[5]=(позиция+20)<<14; B[0]=2.",
     "g.java:12284 g(int,int,int,int)"),
    (169, "set_bM", "STATE", "z[o+0]", "g.bM",
     "g.bM = z[o+0]",
     "Установка переменной bM (управляет циклом J()).",
     "g.java:17663 case 169"),
    (170, "noop", "CONTROL", "-", "-", "-", "Нет операции.", "g.java:17664 case 170"),
    (171, "effect_switch", "GRAPHICS", "z[o+0]", "различные эффекты",
     "g.ab(n): 0->eI(), 1->eK(), 2->g.b(7)+g.d(750,1,1,35), 3->...",
     "Переключатель эффектов: 0/1/2/3+ — разные визуальные/аудио эффекты.",
     "g.java:18592 ab(int)"),
    (172, "object_action2", "OBJECT", "z[o+2],z[o+4],z[o+6],z[o+8]", "объект-тайл",
     "g.b(o+2,o+4,o+6,o+8,var4_4)",
     "Действие над объектом-тайлом (как 112, смещённые аргументы).",
     "g.java:17667 case 172"),
]

SEMANTIC = {op: (name, cls, reads, writes, calls, desc, ev) for op, name, cls, reads, writes, calls, desc, ev in SEM}
KNOWN_OPS = set(SEMANTIC)

# ---------------------------------------------------------------- сборка samples
samples = {}
for mi in range(5):
    sp = json.loads((MISS / f"mission_{mi:02d}" / "special-records.json").read_text())
    for s in sp:
        op = s["opcode"]
        samples.setdefault(op, []).append({
            "mission": f"mission_{mi:02d}", "offset": s["offset"], "len": s["len"],
            "words": s["words"][:12], "attached": "tile" if s["attached_to_tile"]
            else ("object" if s["attached_to_object"] else "none"),
            "tile_index": s["tile_index"], "object_index": s["object_index"],
            "context": s["context"],
        })

SE.mkdir(parents=True, exist_ok=True)
for op, lst in samples.items():
    (SE / "opcode-samples").mkdir(parents=True, exist_ok=True)
    (SE / "opcode-samples" / f"opcode-{op}.json").write_text(
        json.dumps({"opcode": op, "count": len(lst), "samples": lst[:50]},
                   indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- dispatch-trace
dispatch = {"note": "Точный dispatch trace: парсер 16860 записывает [op][len][len x u16] в g.z; "
                    "исполнители g.H() (действия) и g.K() (условия); skip g.n(boolean).",
            "parser": {"method": "g.a(byte[],int,int[],int,int[][][],int)", "line": "g.java:16860",
                       "write": "g.z[v14]=op; g.z[v14+1]=len; g.z[v14+2..]=bytes; g.H[idx]=позиция; g.A[idx]=кол-во"},
            "executor_action": {"method": "g.H()", "line": "g.java:17353",
                                "loop": "while (bQ > 0 && var0 < 150)", "entry": "g.b(int n): bP=n; bO=H[n]; bQ=A[n]"},
            "executor_condition": {"method": "g.K()", "line": "g.java:17740",
                                   "note": "вычисляет условие выполнения опкода (используется в диалог-цикле J())"},
            "skip": {"method": "g.n(boolean)", "line": "g.java:17290",
                     "note": "пропуск if-блока: 145/146 скобки, 143 else, 144 endif; q(n): 124,125,138,140,145,160,167 — ветвящиеся"},
            "terminator": {"opcode": 159, "note": "конец скрипта (J(): while n != 159)"},
            "opcodes": []}
for op in sorted(set(samples) | KNOWN_OPS):
    entry = {"opcode": op, "count_in_missions": len(samples.get(op, [])),
             "missions": sorted({s["mission"] for s in samples.get(op, [])})}
    if op in SEMANTIC:
        name, cls, reads, writes, calls, desc, ev = SEMANTIC[op]
        entry.update({"name": name, "class": cls, "reads": reads, "writes": writes,
                      "calls": calls, "semantics": desc, "evidence": ev})
    else:
        entry.update({"name": None, "semantics": "UNKNOWN (нет case в H()/K()?)", "evidence": None})
    dispatch["opcodes"].append(entry)
(SE / "dispatch-trace.json").write_text(json.dumps(dispatch, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- opcode-master
master = {"meta": {"date": "2026-08-15",
                   "method": "статическая реконструкция из g.H()/g.K()/g.n() и тел методов-действий",
                   "structural_confidence_legend": "CONFIRMED = case найден в исполнителе; "
                                                   "INFERRED = метод-действие прочитан частично",
                   "semantic_confidence_legend": "CONFIRMED = эффект ясен из тела; "
                                                 "INFERRED = частично; UNKNOWN = не установлен; "
                                                 "REQUIRES_REAL_RUNTIME = нужен рантайм"},
          "opcodes": []}
for op in sorted(set(samples) | KNOWN_OPS):
    if op in SEMANTIC:
        name, cls, reads, writes, calls, desc, ev = SEMANTIC[op]
        sem_conf = "CONFIRMED" if op not in (127, 135, 152, 154) else "INFERRED"
        runtime = False
        if op in (118, 127, 135, 147, 148, 152):
            runtime = True
        master["opcodes"].append({
            "opcode": op, "name": name, "class": cls,
            "missions": sorted({s["mission"] for s in samples.get(op, [])}),
            "operand_format": {"opcode_byte": 1, "len_byte": 1, "operands": "len x u16 LE"},
            "dispatch": {"action": "g.H() case %d" % op if op < 150 or op in (150,151,152,153,154,155,156,157,158,159,160,161,162,165,167,168,169,170,171,172) else "g.K() case %d" % op,
                         "condition": ("g.K() case %d" % op) if op in (150,151,152,154,155,156,157,158,159,160,161,162,165,167,168,170,171,172) else None},
            "data_flow": {"reads": reads, "writes": writes, "calls": calls},
            "effect_signature": {"reads": reads, "writes": writes, "calls": calls,
                                 "creates": [], "destroys": [], "state_changes": writes,
                                 "resource_access": [], "confidence": sem_conf},
            "structural_confidence": "CONFIRMED",
            "semantic_confidence": sem_conf,
            "runtime_required": runtime,
            "semantics": desc,
            "evidence": ev,
        })
    else:
        master["opcodes"].append({
            "opcode": op, "name": None, "class": "UNKNOWN",
            "missions": sorted({s["mission"] for s in samples.get(op, [])}),
            "operand_format": {"opcode_byte": 1, "len_byte": 1, "operands": "len x u16 LE"},
            "dispatch": {"action": None, "condition": None},
            "data_flow": {}, "effect_signature": {"confidence": "UNKNOWN"},
            "structural_confidence": "CONFIRMED (в данных)",
            "semantic_confidence": "UNKNOWN",
            "runtime_required": True,
            "semantics": "UNKNOWN (case не найден в прочитанных исполнителях)",
            "evidence": None,
        })
(SE / "opcode-master-v2.json").write_text(json.dumps(master, indent=1, ensure_ascii=False))

# ---------------------------------------------------------------- mission-script-flow
flow_md = """# Mission Script Flow V2 — модель control-flow скриптов миссий

**Дата:** 2026-08-15 · **Источник:** g.H()/g.K()/g.n()/g.b()/g.J() (g.java:17258-17880).

## 1. Структура исполнения

```
g.b(int n)  (вход: индекс скрипта/тайла)
  bP = n; bO = H[n]; bQ = A[n]        // указатель и счётчик (таблицы из парсера 16860)
  -> g.H()                             // исполнитель действий

g.H()  (действия)
  while (bQ > 0 && opcode < 150):     // опкоды 110..149 в цикле
      switch(opcode) -> метод-действие
      bO += 2 + (z[bO+1] << 1)         // следующий опкод
  if (bQ > 0): switch(opcode) { 150..172 }  // опкоды 150+ — однократно

g.n(boolean)  (skip/ветвление)
  опкоды 145/146 — скобки if/else; 143 — else; 144 — endif
  q(n) = {124,125,138,140,145,160,167} — «ветвящиеся» опкоды
  при ложном условии: пропуск до баланса 145/146 (n5 == 0)

g.J() / g.I()  (диалоговый режим)
  while (n != 159 && !K() && bM == -1): K() — проверка условия каждого опкода
  159 = ТЕРМИНАТОР скрипта
```

## 2. Модель

```
ENTRY: g.b(idx) -> bO=H[idx], bQ=A[idx]
  -> ACTION: 110..172 (сущности, объекты, тайлы, состояние, камера, эффекты)
  -> CONDITION: 124/125 (сравнение свойств), K()-проверки для 150..172
  -> BRANCH: 145/146/143/144 (if/else), skip g.n(bl)
  -> DELAY: 117 (wait-цикл), 153 (сброс таймера bV), 119/155 (отложенный вызов)
  -> SUBROUTINE: 123 (bO=H[idx], bQ=A[idx] — вложенный скрипт)
  -> TERMINATOR: 159 (конец)
COMPLETION — REQUIRES_REAL_RUNTIME
```

## 3. Семантические классы (только по доказанному коду)

| Класс | Опкоды | Основание |
| :--- | :--- | :--- |
| ENTITY | 110,111,115,116,118,127,128,130,134,135,141,142,147,148,150,151,152,154,160,162 | g.a/g.b/g.c/g.d/g.e/g.n/g.o/g.f — поиск/команды/спавн/телепорт сущностей |
| TILE | 113,114 | g.j/g.k — поля и команды объектов-тайлов |
| OBJECT | 112,167,172 | g.b — действия над объектами-тайлами |
| STATE | 131,132,139,157,158,161,165,169 | установка глобальных переменных/состояний |
| CONTROL | 117,119,122,123,124,125,129,138,140,143,144,145,146,153,155,159,170 | ветвления, вызовы, ожидания, no-op |
| CAMERA | 156,168 | g.R (скролл), g.g (цель камеры) |
| GRAPHICS | 133,137,171 | g.s (удаление спрайтов), g.i/g.bz (эффект E), g.ab (эффекты) |
| PROGRESSION | 126 | g.ah (очки/деньги L[4]) |
| ANIMATION | 121 | g.cp (стек анимаций) + g.bh (сброс A[]) |
"""
(Path("research/analysis/v2/missions") / "mission-script-flow-v2.md").write_text(flow_md, encoding="utf-8")

# ---------------------------------------------------------------- статистика
n_known = len(KNOWN_OPS)
n_in_data = len(samples)
print(f"опкодов в данных: {n_in_data}; с восстановленной семантикой: {n_known}")
cls_counts = Counter(v[1] for v in SEMANTIC.values())
print("классы:", dict(cls_counts))
print("файлы записаны в", SE)
