# Media Resource Lifecycle V2

```
регистрация: a(byte[], n, n2, n3, bl) (4271):
  a[n] = ByteArrayInputStream(bytes); e[n]=тип; f[n]=формат
  bl=true: createPlayer -> realize() -> prefetch()  (прелоад)
воспроизведение: a(n, 1) (4356):
  Player из a[i[n]] или createPlayer (если null)
  VolumeControl.setLevel(100); setLoopCount(j[n]); start()
остановка: c(n) stop; a() все; ah() фоновый
память: прелоад + переиспользование Player; freeMemory<100000 -> пропуск звука (1042);
  при ошибке: повторный createPlayer (k)
```

## Memory / Performance
- Прелоад: a[] (ByteArrayInputStream), Player создаётся заранее (bl=true).
- Переиспользование: Player кэшируется в b[n].
- 2 канала: музыка + SFX.
- Ограничение: freeMemory < 100000 → звук не играет (геймплей приоритет).
