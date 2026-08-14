/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  java.lang.Integer
 *  java.lang.Math
 *  java.lang.Object
 *  java.lang.System
 *  javax.microedition.lcdui.Graphics
 */
import javax.microedition.lcdui.Graphics;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public final class f {
    public static int a = 0;
    public static int b;
    public static int c;
    public static int d;
    public static int e;
    public static int f;
    public static int g;
    public static int h;
    public static int i;
    public static int j;
    public static int k;
    public static int l;
    public static int m;
    public static int n;
    public static int o;
    public static boolean a;
    public static int p;
    public static int q;
    public static int r;
    public static int s;
    public static f a;
    public static int t;
    public static boolean b;
    public static int u;
    public static int v;
    public static int w;
    public static int x;
    public static boolean c;
    public static boolean d;
    public static boolean e;
    public static int y;
    public static int z;
    public static c[] a;
    public static int[] a;
    public static byte[][] a;
    public static int[] b;
    public static int[] c;
    public static int A;
    public static int B;
    public static int[] d;
    public static int[][] a;
    public static f b;
    public static int C;
    public static int D;
    public static boolean f;
    public static boolean g;
    public static int E;
    public static boolean h;
    public static boolean i;
    public static int F;
    public static int G;
    public static int H;
    public static int I;
    public static int[] e;
    public static f c;
    public static int J;
    public static int[] f;
    public static boolean j;
    public static boolean k;
    public c a;
    public int K;
    public int L;
    public int M;
    public int[] g;

    public static void a() {
        a = 0;
        d = 0;
        h = 2304;
        i = 0;
        j = 0;
        k = 0;
        l = 0;
        n = 1;
        o = 1;
        p = 0;
        q = 0;
        e = -1;
        f = -1;
        r = 0;
        s = 0;
        d = false;
        a = null;
    }

    private static void a(c c2) {
        c2.a();
    }

    public static int a(int n) {
        int n2;
        block16: {
            int n3;
            block13: {
                block15: {
                    block14: {
                        block12: {
                            block11: {
                                int n4;
                                int n5;
                                block10: {
                                    block9: {
                                        int n6;
                                        n2 = 0;
                                        if (((n &= 0x3FDE) & 0x404) != 0) {
                                            n6 = 1028;
                                        } else if ((n & 0x900) != 0) {
                                            n6 = n2 = 2304;
                                        }
                                        if ((n & 0x1010) == 0) break block9;
                                        n5 = n2;
                                        n4 = 4112;
                                        break block10;
                                    }
                                    if ((n & 0x2040) == 0) break block11;
                                    n5 = n2;
                                    n4 = 8256;
                                }
                                n2 = n5 | n4;
                            }
                            if ((n & 2) == 0) break block12;
                            n3 = 5140;
                            break block13;
                        }
                        if ((n & 8) == 0) break block14;
                        n3 = 9284;
                        break block13;
                    }
                    if ((n & 0x80) == 0) break block15;
                    n3 = 6416;
                    break block13;
                }
                if ((n & 0x200) == 0) break block16;
                n3 = 10560;
            }
            n2 = n3;
        }
        return n2;
    }

    private static boolean b() {
        if (g.ez != 0) {
            int n = f.a(g.ez);
            if (d == 0) {
                d = n;
                g.d(e);
                g.d(f);
            } else if (g.a(f, 0)) {
                if ((d & n) == d && (n & ~(d & n)) == 0 && ((n & 0x32DA) != 0 && (n & 0xF8E) == 0 || (n & 0x32DA) == 0 && (n & 0xF8E) != 0)) {
                    d = 0;
                    return true;
                }
                d = n;
                g.d(e);
                g.d(f);
            } else {
                d = 0;
            }
        }
        if (g.a(e, 300)) {
            d = 0;
        }
        return false;
    }

    public static void a(f f2, int n) {
        h = n;
        i = ~h;
        f.a(0, f2);
    }

    public static void a(f f2) {
        if (f2.g[7] <= 0) {
            g.e();
        }
    }

    private static void i() {
        c = 0;
    }

    private static int b(int n, int n2) {
        c += (int)g.d;
        if (n2 != 0) {
            b = ~n2;
        }
        if (c >= 0) {
            b = -1;
            c = 0;
        }
        return n & b;
    }

    private static boolean a(f f2, boolean bl, int n) {
        if (b) {
            g.b(false);
            if (f.c()) {
                f.b(f2);
                f.a(101, f2);
            } else if (bl && n != 0) {
                f.b(f2);
            }
            return true;
        }
        return false;
    }

    private static boolean c() {
        boolean bl = false;
        if (e.a() && e.c()) {
            bl = true;
        }
        r += (int)g.d;
        if (g.ez != 0) {
            ++s;
        }
        if (s >= 5) {
            r = 0;
            s = 0;
            return true;
        }
        if (bl) {
            r = 0;
            s = 0;
            return true;
        }
        if (r >= 2000) {
            r = 0;
            s = 0;
        }
        return false;
    }

    private static void w(f f2) {
        if (f2 != null) {
            switch (f2.L) {
                case 14: {
                    g.b(g.d);
                    g.l(0);
                    return;
                }
                case 0: 
                case 1: 
                case 2: 
                case 11: {
                    g.a(0);
                    return;
                }
                case 16: {
                    g.l(f2);
                    return;
                }
                case 10: {
                    f.A(g.g[g.by][g.bz][f2.g[8]]);
                }
            }
        }
    }

    /*
     * Unable to fully structure code
     */
    public static boolean a(f var0) {
        var1_1 = f.b();
        var2_2 = f.a(g.ez & 16350);
        var3_3 = f.b(f.a(g.ey & 16350), var2_2);
        if (f.n(var0)) {
            var1_1 = false;
        }
        f.z(var0);
        g.h();
        g.f();
        g.h(var0);
        g.d();
        v0 = f.g = f.j != 0 || f.k != 0 ? 0 : f.g + (int)g.d;
        if ((f.p & 4) != 0) {
            g.a[17].a();
        }
        var5_4 = f.a(var0, var1_1, var2_2);
        var6_5 = false;
        block0 : switch (f.a) {
            case 5: {
                if (f.m > 0) {
                    if ((f.m -= (int)g.d) > 0) {
                        var6_5 = true;
                    } else {
                        f.a(0, var0);
                    }
                }
            }
            case 0: {
                if (!var5_4) {
                    g.a(var0, f.h, false, false);
                }
                if (g.X) {
                    v1 = 9;
                } else if (g.Z) {
                    v1 = g.L[1] != -1 ? 12 : 13;
                } else if (var2_2 != 0 && !var1_1) {
                    f.a(var2_2);
                    v1 = f.a;
                } else if (var3_3 != 0 || var1_1 && var2_2 != 0) {
                    if (var1_1 && var2_2 != 0) {
                        f.a(var2_2);
                        f.i();
                        v1 = 2;
                    } else {
                        f.a(var3_3);
                        v1 = var6_5 ? 3 : 1;
                    }
                } else {
                    if ((g.ez & 16416) != 0 && g.d != null) {
                        f.w(g.d);
                        break;
                    }
                    v1 = !f.b && g.a(true) != null && g.L[1] != -1 ? 6 : (!f.b && (g.ez & 16416) != 0 && g.L[1] != -1 ? 6 : (g.W ? 17 : f.a));
                }
                ** GOTO lbl321
            }
            case 18: {
                v1 = 18;
                ** GOTO lbl321
            }
            case 6: {
                g.a(var0, f.h, true, true);
                if (g.b()) {
                    if ((var3_3 & 16350) == 0) break;
                    f.a(var3_3);
                    v1 = 7;
                } else if (g.a(true) != null) {
                    if ((var3_3 & 16350) == 0) {
                        g.cu = g.h(f.a(var0, g.a(true), true));
                        f.c(var0);
                    }
                    if ((g.ez & 16416) != 0 && g.d != null) {
                        f.w(g.d);
                        break;
                    }
                    if (g.X) {
                        v1 = 9;
                    } else if (g.V) {
                        g.cu = g.h(f.a(var0, g.a(true), true));
                        v1 = 8;
                    } else if (g.W) {
                        v1 = 17;
                    } else if (g.Z) {
                        v1 = g.L[1] != -1 ? 12 : 13;
                    } else if ((var2_2 & 16350) != 0) {
                        var11_6 = g.h(var2_2);
                        if (var1_1 && var2_2 != 0) {
                            f.a(var2_2);
                            f.i();
                            v1 = 2;
                        } else {
                            if (var11_6 == g.cu || g.i(var11_6) == 0) break;
                            f.a(var2_2);
                            g.cu = var11_6;
                            g.f(var0);
                            v1 = 6;
                        }
                    } else {
                        if ((var3_3 & 16350) == 0) break;
                        var11_7 = g.h(var3_3);
                        if (var11_7 != g.cu && g.i(var11_7) != 0) {
                            f.a(var3_3);
                            g.cu = var11_7;
                            g.f(var0);
                            v1 = 6;
                        } else {
                            f.a(var3_3);
                            v1 = 7;
                        }
                    }
                } else {
                    if ((g.ez & 16416) != 0 && g.d != null) {
                        f.w(g.d);
                        break;
                    }
                    if (g.X) {
                        v1 = 9;
                    } else if (g.V) {
                        v1 = 8;
                    } else if (g.W) {
                        v1 = 17;
                    } else if (g.Z) {
                        v1 = g.L[1] != -1 ? 12 : 13;
                    } else {
                        if ((var2_2 & 16350) == 0) break;
                        f.a(var2_2);
                        v1 = 1;
                    }
                }
                ** GOTO lbl321
            }
            case 7: {
                g.a(var0, f.h, true, false);
                if (g.b()) {
                    if ((var2_2 | var3_3) != 0) {
                        f.a(var3_3);
                        v1 = 7;
                    } else {
                        v1 = 6;
                    }
                } else if (g.a(true) != null) {
                    g.cu = g.h(f.a(var0, g.a(true), true));
                    f.c(var0);
                    if (var3_3 != 0) {
                        f.a(var3_3);
                        v1 = (f.l += (int)g.d) >= 1000 ? 3 : 7;
                    } else if (var1_1) {
                        f.a(var2_2);
                        v1 = 3;
                    } else {
                        v1 = 6;
                    }
                } else {
                    if (var3_3 != 0) {
                        f.a(var3_3);
                    }
                    v1 = 1;
                }
                ** GOTO lbl321
            }
            case 8: {
                var7_8 = g.l(g.L[1], 21);
                g.c(false);
                switch (var7_8) {
                    case 4: {
                        var8_9 = g.a(true);
                        if ((g.ey & 16416) == 0 || g.a()) {
                            v1 = 0;
                            break;
                        }
                        g.a(var0, var8_9, g.L[1]);
                        break block0;
                    }
                    case 6: {
                        if ((g.ey & 16416) != 0) {
                            if (!var0.a.a()) break block0;
                            f.a(7, var0);
                            g.L[3] = 2;
                            break block0;
                        }
                        v1 = 0;
                        break;
                    }
                    default: {
                        if (var3_3 != 0) {
                            f.a(var3_3);
                            v1 = 1;
                            break;
                        }
                        if (!var0.a.a()) break block0;
                        v1 = 6;
                        break;
                    }
                }
                ** GOTO lbl321
            }
            case 9: {
                if (var3_3 != 0 || var1_1 && var2_2 != 0) {
                    if (var1_1 && var2_2 != 0) {
                        f.a(var2_2);
                        v1 = 2;
                    } else {
                        f.a(var3_3);
                        v1 = 1;
                    }
                } else {
                    if (!var0.a.a() && g.X) break;
                    v1 = 0;
                }
                ** GOTO lbl321
            }
            case 12: {
                if (var3_3 != 0) {
                    f.a(var3_3);
                    v1 = 1;
                } else {
                    if (!var0.a.a()) break;
                    v1 = 13;
                }
                ** GOTO lbl321
            }
            case 13: {
                if (var3_3 == 0) ** GOTO lbl202
                f.a(var3_3);
                v1 = 1;
                ** GOTO lbl321
lbl202:
                // 1 sources

                if (!var0.a.a()) break;
                ** GOTO lbl320
            }
            case 1: {
                g.c(false);
                if (!var1_1 || var2_2 == 0) ** GOTO lbl211
                f.a(var2_2);
                f.i();
                v1 = 2;
                ** GOTO lbl321
lbl211:
                // 1 sources

                if (var3_3 == 0) ** GOTO lbl320
                f.i();
                f.a(var3_3);
                v1 = (f.l += (int)g.d) >= 300 || g.ct >= 1 ? 3 : 1;
                ** GOTO lbl321
            }
            case 2: {
                g.c(false);
                if (var0.a.a()) {
                    if (var3_3 != 0 && (var3_3 & f.h) != 0) {
                        v1 = 3;
                    } else {
                        if (var3_3 != 0) {
                            f.a(var3_3);
                        }
                        v1 = 1;
                    }
                } else {
                    v1 = 2;
                }
                ** GOTO lbl321
            }
            case 3: {
                g.c(false);
                if ((g.ez & 16416) != 0) {
                    if (g.d != null) {
                        f.a(0, var0);
                        f.w(g.d);
                        break;
                    }
                    if (!f.m(var0)) break;
                    v1 = 14;
                } else if (var1_1 && var2_2 != 0) {
                    f.a(var2_2);
                    f.i();
                    v1 = 2;
                } else if (var3_3 == 0 || ((var3_3 | f.h) & 3332 ^ 3332) == 0 || ((var3_3 | f.h) & 12368 ^ 12368) == 0) {
                    v1 = 4;
                } else {
                    f.i();
                    f.a(var3_3);
                    v1 = 3;
                }
                ** GOTO lbl321
            }
            case 4: {
                g.c(false);
                if (var3_3 == 0) {
                    if (var2_2 != 0) {
                        f.a(var2_2);
                    }
                    if ((g.ez & 16416) != 0 && g.d != null) {
                        f.a(0, var0);
                        f.w(g.d);
                        break;
                    }
                    if ((g.ez & 16416) != 0 && f.m(var0)) {
                        v1 = 14;
                    } else if (!f.b && (g.ez & 16416) != 0 && g.L[1] != -1) {
                        v1 = 6;
                    } else if (f.j == 0 && f.k == 0) {
                        f.m = 500;
                        v1 = 5;
                    } else {
                        v1 = 4;
                    }
                } else {
                    f.a(var3_3);
                    if ((f.h & 13018) != 0) {
                        f.j = 1474560;
                    }
                    if ((f.h & 3982) != 0) {
                        f.k = 1474560;
                    }
                    v1 = 3;
                }
                ** GOTO lbl321
            }
            case 14: {
                if ((f.v += (int)g.d) >= 400) {
                    f.x(var0);
                }
                if (var0.a.a()) ** GOTO lbl320
                v1 = 14;
                ** GOTO lbl321
            }
            case 11: {
                v1 = 11;
                ** GOTO lbl321
            }
            case 15: {
                if ((g.e() || var0.a.a()) && g.dZ != 2) {
                    g.j(var0);
                }
                if (!var0.a.a()) break;
                ** GOTO lbl320
            }
            case 17: {
                if ((f.v += (int)g.d) >= 100) {
                    g.f(var0);
                    f.y(var0);
                }
                if (!var0.a.a()) break;
                ** GOTO lbl320
            }
            case 100: {
                f.c(var0);
                g.f(var0);
                if (!g.a(g.a(false, false), true)) ** GOTO lbl305
                g.W = true;
                v1 = 17;
                ** GOTO lbl321
lbl305:
                // 1 sources

                if (!f.c()) break;
                f.a(101, var0);
                f.b(var0);
                break;
            }
            case 101: {
                if (!var0.a.a()) break;
                ** GOTO lbl320
            }
            case 666: {
                if (!var0.a.a()) break;
                g.a(0);
                g.a(20, true);
                break;
            }
            case 16: {
                if ((f.w += (int)g.d) < 800) break;
                f.w = 0;
lbl320:
                // 7 sources

                v1 = 0;
lbl321:
                // 52 sources

                f.a(v1, var0);
            }
        }
        var9_10 = (int)g.d;
        v2 = var10_11 = f.a(var0, f.h, f.j * var9_10, f.k * var9_10, 819200 * var9_10 / 1000) == false;
        if (f.a == 7 || f.a == 6 || f.a == 18) {
            f.a(g.c());
        }
        return var10_11;
    }

    public static void b(f f2) {
        a = null;
        t = 0;
        b = false;
        for (int i = 0; i < g.cg; ++i) {
            boolean bl;
            f f3;
            int n;
            if (g.e[i].L != 3 || g.e[i].g[12] >= 100 || g.e[i].g[10] == 5 || (n = g.a(f2, f3 = g.e[i])) >= 1600 || (bl = g.a(f2.a.a, f2.a.b, g.e[i].a.a, g.e[i].a.b, null, false, 133))) continue;
            f.i(f3);
            f.c(f3, 9);
        }
    }

    private static boolean m(f f2) {
        if ((g.e & 2) != 0 && !f.n(f2)) {
            g.f(f2);
            g.a(f2, h, false, false);
            f f3 = g.a();
            return f2.g[18] == 1 && g.K[g.cu] > 0 && f3 != null && f3.M <= 4096;
        }
        return false;
    }

    private static void x(f f2) {
        for (int i = 0; i < g.cg; ++i) {
            int n;
            if (g.e[i].L != 3 || g.e[i].g[12] >= 100 || g.e[i].g[12] == 14 || g.e[i].g[12] == 9) continue;
            f f3 = g.e[i];
            int n2 = g.h(f3.g[0], 10);
            if (f.d(f3) || (n = g.a(f2, f3)) >= 1600 || g.a(f2.a.a, f2.a.b, g.e[i].a.a, g.e[i].a.b, null, false, 133)) continue;
            if ((n2 == 4 || n2 == 6) && f3.g[12] != 7 && f3.g[12] != 8 && f3.g[12] != 19 && f3.g[12] != 18) {
                f.f(f3, g.c.a.a, g.c.a.b, 0);
                f.c(f3, 18);
                f.c(f3);
                continue;
            }
            int n3 = f.a(f2, f3, false);
            if ((n3 & h) == 0) continue;
            int[] nArray = g.b(f3.a);
            int n4 = (nArray[3] - nArray[1] >> 2) * 3;
            int n5 = f.b(f3, 1);
            f.i(f3);
            f.a(f3, n5, -1, g.k[f2.g[4]][5], true, 0, -n4, -1, true);
            if (f.c(f3, n5, -1) > 0) {
                f.c(f3, 9);
                continue;
            }
            f.G(f3);
            f.I(f3);
        }
    }

    public static boolean a() {
        return a != 100 && a != 16 && a != 10 && a != 11 && a != 15 && f.e(g.c) != -1;
    }

    private static void y(f f2) {
        f f3 = g.a(false, false);
        if (g.W && f3 != null && g.a(f3, false)) {
            f.i(f3);
            int n = f.b(f3, 1);
            f.f(f3, f2.a.a, f2.a.b, 0);
            f.a(f3, n, -1, 100, true, 0, 0, -1, true);
            f.G(f3);
            f.I(f3);
            g.b(14);
        }
        g.W = false;
    }

    public static void a(int n, int[] nArray) {
        int n2 = nArray[0] + (nArray[2] - nArray[0] >> 1);
        int n3 = nArray[1] + (nArray[3] - nArray[1] >> 1);
        int n4 = g.b(n2);
        int n5 = g.b(n3);
        int n6 = g.b(n);
        for (int i = -n6; i <= n6; ++i) {
            block5: for (int j = -n6; j <= n6; ++j) {
                f f2 = g.a(n4 + i, n5 + j);
                if (f2 == null) continue;
                switch (f2.L) {
                    case 3: {
                        f.E(f2);
                        continue block5;
                    }
                    case 9: {
                        f.k(f2);
                    }
                }
            }
        }
    }

    public static void b(f f2, int n) {
        f.a(f2, n, false);
    }

    public static int a(int n, int n2) {
        return n * 30 / 100 * n2;
    }

    private static void a(f f2, int n, boolean bl) {
        if (!d) {
            if ((p & 2) == 0 || bl) {
                g.b(f2.g[4] == 3 ? 23 : 22);
                int n2 = f.a(n, g.bF);
                f2.g[7] = f2.g[7] - (n += n2);
                p |= 2;
                u = 0;
                g.i();
            }
            g.i(n);
        }
    }

    public static void b() {
        if ((p & 2) != 0 && (u += (int)g.d) >= 2000) {
            p &= 0xFFFFFFFD;
            u = 0;
        }
    }

    private static boolean a(int n) {
        int n2 = 0;
        if (n != -1) {
            n2 = g.b[n][15];
        }
        return n2 >= 3;
    }

    private static boolean n(f f2) {
        int n = f2.g[28];
        int n2 = -1;
        if (n > -1) {
            n2 = g.l(n, 18);
        }
        return f.a(n2);
    }

    private static int b(int n) {
        int n2 = g.l(g.L[1], 18);
        short s = g.b[n2][15];
        if (s >= 3) {
            int n3 = (s - 3 + 1) * 10;
            n -= n * n3 / 100;
        }
        return n;
    }

    public static void a(int n, f f2) {
        if (a != n || i != h) {
            switch (n) {
                case 14: 
                case 17: {
                    v = 0;
                    break;
                }
                case 1: 
                case 7: {
                    if (n == a) break;
                    l = 0;
                    break;
                }
                case 100: {
                    r = 0;
                    s = 0;
                    break;
                }
                case 0: {
                    break;
                }
                case 8: {
                    int n2 = g.l(g.L[1], 12);
                    if (n2 == -1) break;
                    p |= 1;
                    break;
                }
                case 13: {
                    g.g();
                }
            }
            a = n;
            f.c(f2);
            if (a == 9) {
                if (g.Y) {
                    g.j(g.b(f2));
                    g.Y = false;
                }
                g.g(f2);
            }
            if (a != 4) {
                i = h;
            }
        }
        int n3 = (int)g.d;
        boolean bl = f2.g[9] == 1 && g.b == 0;
        int n4 = f.b((bl ? 0x104000 : 983040) / 1000);
        int n5 = f.b((bl ? 1802240 : 1474560) / 1000);
        int n6 = 0;
        int n7 = 0;
        int n8 = 0;
        int n9 = 16384 * n3 / 1000;
        switch (a) {
            case 18: {
                int n10 = f.a((g.ez | g.ey) & 0x3FDE);
                if (!g.c() || n10 == 0) break;
                f.a(n10);
            }
            case 1: 
            case 7: {
                n8 = n4;
                int n11 = n6 = (h & 0x32DA) != 0 ? 983040 * n3 / 1000 : -j;
                if ((h & 0xF8E) != 0) {
                    n7 = 983040 * n3 / 1000;
                    break;
                }
                n7 = -k;
                break;
            }
            case 2: {
                n8 = 2457;
                int n12 = n6 = (h & 0x32DA) != 0 ? 0x1E0000 * n3 / 1000 : -j;
                if ((h & 0xF8E) != 0) {
                    n7 = 0x1E0000 * n3 / 1000;
                    break;
                }
                n7 = -k;
                break;
            }
            case 3: 
            case 14: {
                int n13;
                n8 = n5;
                if ((h & 0x32DA) != 0) {
                    n6 = 1474560 * n3 / 1000;
                    if (n6 < n4) {
                        n13 = n4;
                    }
                } else {
                    n13 = n6 = 0 - j;
                }
                if ((h & 0xF8E) != 0) {
                    n7 = 1474560 * n3 / 1000;
                    if (n7 >= n4) break;
                    n7 = n4;
                    break;
                }
                n7 = 0 - k;
                break;
            }
            case 4: {
                n8 = n5;
                n6 = -n9;
                n7 = -n9;
                break;
            }
            case 10: {
                g.b(f2, true);
                break;
            }
            case 11: {
                g.b(f2, false);
                break;
            }
            case 16: {
                int n14 = f.d(f2);
                j = g.d(f2.g[n14 + 11] * 80) / 1000;
                f.n = f2.g[n14 + 11] < 0 ? -1 : 1;
                k = g.d(f2.g[n14 + 12] * 80) / 1000;
                o = f2.g[n14 + 12] < 0 ? -1 : 1;
                n8 = j > k ? j : k;
                w = 0;
                break;
            }
            default: {
                j = 0;
                k = 0;
            }
        }
        if (d) {
            n8 <<= 1;
        }
        if ((j += n6) < 0) {
            j = 0;
        }
        if (j > n8) {
            j = n8;
        }
        if ((k += n7) < 0) {
            k = 0;
        }
        if (k > n8) {
            k = n8;
        }
    }

    public static void a(int n) {
        block8: {
            int n2;
            block7: {
                block6: {
                    int n3;
                    h = n;
                    if ((h & 0x1010) != 0) {
                        n3 = -1;
                    } else if ((h & 0x2040) != 0) {
                        n3 = f.n = 1;
                    }
                    if ((h & 0x404) == 0) break block6;
                    n2 = -1;
                    break block7;
                }
                if ((h & 0x900) == 0) break block8;
                n2 = 1;
            }
            o = n2;
        }
    }

    public static int a() {
        return 0;
    }

    public static void c(f f2) {
        f.a(f2, a, g.cu, h, f2.g[28], f2.g[29]);
    }

    private static int c(int n) {
        int n2;
        block6: {
            int n3;
            block3: {
                block5: {
                    block4: {
                        block2: {
                            n2 = 0;
                            if ((n & 0x1010) == 0) break block2;
                            n3 = 2;
                            break block3;
                        }
                        if ((n & 0x2040) == 0) break block4;
                        n3 = 3;
                        break block3;
                    }
                    if ((n & 0x404) == 0) break block5;
                    n3 = 0;
                    break block3;
                }
                if ((n & 0x900) == 0) break block6;
                n3 = 1;
            }
            n2 = n3;
        }
        return n2;
    }

    /*
     * Unable to fully structure code
     */
    public static int a(f var0, int var1_1, int var2_2, int var3_3, int var4_4, int var5_5) {
        var6_6 = 0;
        var7_7 = true;
        var6_6 = f.c(var3_3);
        switch (var1_1) {
            case 8: {
                v0 = f.c ? 116 : 88;
                ** GOTO lbl95
            }
            case 0: 
            case 5: {
                if (var4_4 > -1) {
                    v0 = 64;
                    v1 = g.h(var3_3);
                } else {
                    v0 = 56;
                    v1 = g.h(var3_3);
                }
                ** GOTO lbl96
            }
            case 1: {
                if (var4_4 > -1) {
                    var6_6 += 72;
                    break;
                }
                var6_6 += 48;
                break;
            }
            case 2: {
                var7_7 = false;
                v0 = 24;
                v1 = g.h(var3_3);
                ** GOTO lbl96
            }
            case 14: {
                var7_7 = false;
                v0 = 16;
                v1 = g.h(var3_3);
                ** GOTO lbl96
            }
            case 15: {
                var7_7 = false;
                if (g.k[var0.g[4]][6] == -1) {
                    var6_6 += 40;
                    break;
                }
                v0 = 16;
                v1 = g.h(var3_3);
                ** GOTO lbl96
            }
            case 3: 
            case 4: {
                if (var4_4 > -1) {
                    var6_6 += 76;
                    break;
                }
                var6_6 += 52;
                break;
            }
            case 16: {
                var6_6 += f.f(var0);
                var7_7 = false;
                break;
            }
            case 100: {
                var7_7 = false;
                if (f.s == 0) {
                    var6_6 += 8;
                    break;
                }
                var6_6 += 44;
                break;
            }
            case 666: {
                var7_7 = false;
                v2 = 7;
                break;
            }
            case 9: {
                var6_6 += 104;
                break;
            }
            case 12: {
                var6_6 += 108;
                break;
            }
            case 13: {
                var6_6 += 112;
                break;
            }
            case 101: {
                var7_7 = false;
                var6_6 += 12;
                break;
            }
            case 6: {
                v0 = 80;
                ** GOTO lbl95
            }
            case 7: {
                v0 = 96;
                ** GOTO lbl95
            }
            case 10: {
                var7_7 = false;
                var6_6 += 36;
                break;
            }
            case 11: {
                var7_7 = false;
                var6_6 += 32;
                break;
            }
            case 17: {
                var7_7 = false;
                var6_6 += 40;
                break;
            }
            case 18: {
                var7_7 = false;
                v0 = g.a(var0, var5_5);
lbl95:
                // 4 sources

                v1 = var2_2;
lbl96:
                // 6 sources

                v2 = var6_6 = v0 + v1;
            }
        }
        if (var7_7) {
            var6_6 += g.k(var4_4);
        }
        if (var0 != null && (var6_6 += f.a()) != var0.a.d && (var0.a.a == null || var6_6 < var0.a.a.h.length)) {
            var0.a.b(var6_6);
        }
        return var6_6;
    }

    public static int a(f f2, f f3, boolean bl) {
        boolean bl2 = true;
        if (f3 != null && f3.L >= 0 && f3.L < 9) {
            bl2 = false;
        }
        return f.a(f2, f3, bl, bl2);
    }

    private static int a(f f2, f f3, boolean bl, boolean bl2) {
        int n = 0;
        if (f3 != null && f2 != null) {
            int n2;
            int n3;
            int n4 = f3.a.a;
            int n5 = f3.a.b;
            if (bl2) {
                int[] nArray = g.a(f3);
                n4 = nArray[0] + (nArray[2] - nArray[0] >> 1) << 14;
                n5 = nArray[1] + (nArray[3] - nArray[1] >> 1) << 14;
            }
            if (g.c(0, n3 = g.b(f2.a.a, f2.a.b, n4, n5))) {
                n2 = 8256;
            } else if (g.c(1, n3)) {
                n2 = 9284;
            } else if (g.c(2, n3)) {
                n2 = 1028;
            } else if (g.c(3, n3)) {
                n2 = 5140;
            } else if (g.c(4, n3)) {
                n2 = 4112;
            } else if (g.c(5, n3)) {
                n2 = 6416;
            } else if (g.c(6, n3)) {
                n2 = 2304;
            } else if (g.c(7, n3)) {
                n2 = n = 10560;
            }
            if (bl) {
                f.a(n);
            }
        }
        return n;
    }

    private static boolean b(f f2, int n, int n2) {
        f f3 = g.a(n, n2);
        boolean bl = false;
        if (f3 != null && f3 != f2) {
            int n3 = g.d(n, n2);
            int n4 = g.e(n, n2);
            g.c(f3);
            g.a(f3, 1, true);
            switch (f3.L) {
                case 0: 
                case 1: {
                    int n5 = f.d(f3);
                    if (f.e(f3) != 2 && f.e(f3) != 4 || (f3.g[n5 + 14] & 0x20) != 0 || !f.j(f3)) break;
                    int n6 = n5 + 14;
                    f3.g[n6] = f3.g[n6] | 0x20;
                    int n7 = f3.g[n5 + 11];
                    int n8 = f3.g[n5 + 12];
                    int n9 = f3.a.a;
                    int n10 = f3.a.b;
                    f3.a.c(g.c(g.b(f3.a.a())) + 8);
                    f3.a.d(g.c(g.b(f3.a.b())) + 8);
                    f.g(f3, g.c(g.b(f2.a.a())) + 8 << 14, g.c(g.b(f2.a.b())) + 8 << 14, 1);
                    f3.a.a = n9;
                    f3.a.b = n10;
                    bl = f.e(f3, 60);
                    if (!bl) {
                        int n11;
                        f f4;
                        if (!f.o(f3)) {
                            f3.a.c(g.c(g.b(f3.a.a())) + 8);
                            f3.a.d(g.c(g.b(f3.a.b())) + 8);
                            n7 = f3.g[n5 + 11];
                            n8 = f3.g[n5 + 12];
                            f4 = f3;
                            n11 = 1;
                        } else {
                            f4 = f3;
                            n11 = 0;
                        }
                        f.d(f4, n11);
                    }
                    f3.g[n5 + 11] = n7;
                    f3.g[n5 + 12] = n8;
                }
            }
            g.a(f3, 0, true);
            g.a(f3, n3, n4);
        }
        return bl;
    }

    private static boolean o(f f2) {
        int n = f2.a.a();
        int n2 = f2.a.b();
        boolean bl = false;
        bl = false | f.b(f2, g.b(n), g.b(n2));
        bl |= f.b(f2, g.b(n - 8), g.b(n2 + 8));
        bl |= f.b(f2, g.b(n + 8), g.b(n2 + 8));
        bl |= f.b(f2, g.b(n - 8), g.b(n2 - 8));
        return bl |= f.b(f2, g.b(n + 8), g.b(n2 - 8));
    }

    private static boolean a(f f2, int n, int n2, int n3, int n4) {
        int n5;
        int n6;
        int n7 = n2;
        a = false;
        c c2 = f2.a;
        for (int i = n3; n7 > 0 || i > 0; n7 -= n6, i -= n5) {
            block17: {
                int n8;
                block15: {
                    int n9;
                    block21: {
                        int n10;
                        block23: {
                            c c3;
                            int n11;
                            block22: {
                                int n12;
                                block18: {
                                    int n13;
                                    block20: {
                                        c c4;
                                        block19: {
                                            block16: {
                                                n9 = c2.a >> 14;
                                                n8 = c2.b >> 14;
                                                n6 = n7 > 131072 ? 131072 : n7;
                                                n5 = i > 131072 ? 131072 : i;
                                                c2.b += n5 * o;
                                                c2.a += n6 * f.n;
                                                if ((n & 0x404) != 0) {
                                                    n8 = g.c(g.b(n8)) + 8;
                                                }
                                                if ((n & 0x900) != 0) {
                                                    n8 = g.c(g.b(n8)) + 8;
                                                }
                                                if ((n & 0x1010) != 0) {
                                                    n9 = g.c(g.b(n9)) + 8;
                                                }
                                                if ((n & 0x2040) != 0) {
                                                    n9 = g.c(g.b(n9)) + 8;
                                                }
                                                if (!f.a(c2.a(), c2.b())) continue;
                                                f.o(f2);
                                                if ((n & 0x3050) != 0 && !f.a(c2.a(), n8)) break block15;
                                                if ((n & 0xD04) == 0 || f.a(n9, c2.b())) break block16;
                                                c2.a = n9 << 14;
                                                break block17;
                                            }
                                            if ((n & 0xD04) == 0) break block18;
                                            n11 = g.d(16 - (n9 - 8 - g.c(g.b(n9 - 8))));
                                            n12 = g.d(n9 + 8 - g.c(g.b(n9 + 8)));
                                            if (n11 == 0) {
                                                n11 = 8;
                                            }
                                            if (f.a(n9 + n11, c2.b())) break block19;
                                            c4 = c2;
                                            n13 = (n9 << 14) + n4;
                                            break block20;
                                        }
                                        if (f.a(n9 - n12, c2.b())) break block18;
                                        c4 = c2;
                                        n13 = (n9 << 14) - n4;
                                    }
                                    c4.a = n13;
                                    c2.b = n8 << 14;
                                    a = true;
                                }
                                if ((n & 0x3050) == 0) break block21;
                                n11 = g.d(n8 + 8 - g.c(g.b(n8 + 8)));
                                n12 = g.d(16 - (n8 - 8 - g.c(g.b(n8 - 8))));
                                if (f.a(c2.a(), n8 + n12)) break block22;
                                c2.a = n9 << 14;
                                c3 = c2;
                                n10 = (n8 << 14) + n4;
                                break block23;
                            }
                            if (f.a(c2.a(), n8 - n11)) break block21;
                            c2.a = n9 << 14;
                            c3 = c2;
                            n10 = (n8 << 14) - n4;
                        }
                        c3.b = n10;
                        a = true;
                    }
                    if (a) break block17;
                    c2.a = n9 << 14;
                }
                c2.b = n8 << 14;
            }
            return false;
        }
        return true;
    }

    public static boolean a(int n, int n2) {
        int n3 = 13;
        if (g.b != 0) {
            n3 = 5;
        }
        return g.b(g.b(n), g.b(n2), n3) || g.b(g.b(n - 8), g.b(n2 + 7), n3) || g.b(g.b(n + 7), g.b(n2 + 7), n3) || g.b(g.b(n - 8), g.b(n2 - 8), n3) || g.b(g.b(n + 7), g.b(n2 - 8), n3);
    }

    public static boolean a(f f2, f f3) {
        if (f3 != null && f2 != null) {
            int n = g.b(f3.a.a());
            int n2 = g.b(f3.a.b());
            int n3 = 1;
            int n4 = 1;
            if (f3.L == 10) {
                --n;
                --n2;
                n3 = f3.g[2] + 2;
                n4 = f3.g[3] + 2;
            }
            int n5 = f2.a.a();
            int n6 = f2.a.b();
            for (int i = 0; i < n3; ++i) {
                for (int j = 0; j < n4; ++j) {
                    if (!(n + i == g.b(n5) && n2 + j == g.b(n6) || n + i == g.b(n5 + 8) && n2 + j == g.b(n6 + 8) || n + i == g.b(n5 - 8) && n2 + j == g.b(n6 + 8) || n + i == g.b(n5 + 8) && n2 + j == g.b(n6 - 8)) && (n + i != g.b(n5 - 8) || n2 + j != g.b(n6 - 8))) continue;
                    return true;
                }
            }
        }
        return false;
    }

    private static void c(Graphics graphics, f f2) {
        if (a == 10 || a == 11) {
            f2.a.a += g.ee;
            f2.a.b += g.ef;
        }
        f.a(graphics, f2, f2.a.a(), f2.a.b(), true);
        f.b(graphics, f2, true);
        f2.a.a.e = f2.g[2];
        f.a(graphics, 0, f2.a.a >> 14, f2.a.b >> 14);
        f2.a.a.a(g.a(f2));
        f2.a.a(graphics);
        f.a(graphics, f2, f2.a.a(), f2.a.b(), false);
        f.b(graphics, f2, false);
    }

    private static void a(Graphics graphics, f f2, int n, int n2, boolean bl) {
        if ((p & 1) != 0 && (bl && (h & 0x404) != 0 || !bl && (h & 0x404) == 0)) {
            int n3 = g.cu + 5;
            g.e(16);
            int[] nArray = f.a(f2, false, true);
            g.a[15].a(graphics, n3, n - nArray[0], n2 - nArray[1], 0);
            g.f(16);
            if ((q += (int)g.d) >= 100) {
                q = 0;
                p &= 0xFFFFFFFE;
            }
        }
    }

    private static void b(f f2, f f3, boolean bl) {
        int n;
        int[] nArray;
        int n2;
        int n3 = f.d(f2);
        if (bl) {
            f.g(f2, f3.a.a, f3.a.b, 0);
            int n4 = n3 + 11;
            f2.g[n4] = f2.g[n4] * -1;
            int n5 = n3 + 12;
            n2 = n5;
            nArray = f2.g;
            n = f2.g[n5] * -1;
        } else {
            f2.g[n3 + 11] = f3.g[13];
            f2.g[n3 + 12] = f3.g[14];
            int n6 = f3.g[13] << 14;
            int n7 = f3.g[14] << 14;
            int n8 = g.b(-n7, n6) * 57 >> 14;
            g.a();
            g.a();
            f2.g[n3 + 11] = g.e(n8) << 6;
            nArray = f2.g;
            n2 = n3 + 12;
            n = -(g.f(n8) << 6);
        }
        nArray[n2] = n;
        f.a(16, f2);
    }

    private static void a(int n, int n2) {
        block2: {
            block7: {
                int n3;
                block4: {
                    block6: {
                        block5: {
                            block3: {
                                if ((p & 4) != 0) break block2;
                                p |= 4;
                                if (n <= 8192) break block3;
                                n3 = 8256;
                                break block4;
                            }
                            if (n >= -8192) break block5;
                            n3 = 4112;
                            break block4;
                        }
                        if (n2 <= 8192) break block6;
                        n3 = 2304;
                        break block4;
                    }
                    if (n2 >= -8192) break block7;
                    n3 = 1028;
                }
                x = n3;
            }
            int n4 = f.c(x);
            g.a[17].b(n4);
        }
    }

    private static void b(Graphics graphics, f f2, boolean bl) {
        if (!g.N && (p & 4) != 0 && (bl && (x & 0x404) != 0 || !bl && (x & 0x404) == 0)) {
            int[] nArray = g.b(f2.a);
            int n = nArray[3] - nArray[1];
            g.a[17].a = f2.a.a;
            g.a[17].b = f2.a.b - (n >> 1 << 14);
            g.a[17].a(graphics);
        }
        if (g.a[17].a()) {
            p &= 0xFFFFFFFB;
        }
    }

    private static boolean d() {
        return j != 0 || k != 0;
    }

    private static boolean e() {
        return a == 18 && g.m(g.M[0], 1) == 1;
    }

    private static void z(f f2) {
        int n;
        if (f2.g[7] < 200 && (g.ez & 0x80000) != 0 && (n = g.c(g.bt, 7)) != -1) {
            byte by = g.c[g.bt][n];
            g.c(by, 1, g.bt, n);
        }
    }

    public static int[] a(f f2, boolean bl, boolean bl2) {
        int n;
        int n2;
        int n3;
        int[] nArray = g.s;
        g.s[0] = 0;
        nArray[1] = 0;
        int n4 = 0;
        int n5 = 0;
        int n6 = 0;
        a a2 = f2.a.a;
        if (bl) {
            n4 = f2.a.d;
            n5 = a2.b(n4, f2.a.e);
            n3 = f2.a.e;
        } else {
            n2 = h;
            n = g.cu;
            if (f2 != g.c) {
                n = f.a(f2, true);
                n2 = g.j(n);
            }
            n4 = f.a(null, 8, n, n2, f2.g[28], f2.g[29]);
            n5 = g.a(f2.a, n4);
            n3 = 0;
        }
        n6 = n3;
        int n7 = a2.h[n4] + n6;
        int n8 = a2.b[n5] & 0xFF;
        int n9 = g.a(a2, n4, 0);
        for (n2 = 0; n2 < n8; ++n2) {
            n = a2.e[n5] + n2;
            int n10 = a2.d[n] & 0xFF;
            int n11 = a2.c[n] & 0xFF;
            if (a2.k[n11 |= (n10 & 0xC0) << 2] != 1) continue;
            a2.b(g.r, n5, n2, 0, 0, n9);
            nArray[0] = -(g.r[0] + a2.i[n7]);
            nArray[1] = -(g.r[1] + a2.j[n7]);
            return nArray;
        }
        if (bl2) {
            int[] nArray2 = g.b(f2.a);
            n = nArray2[3] - nArray2[1];
            n -= n >> 2;
            nArray[0] = 0;
            nArray[1] = n;
        } else {
            nArray = null;
        }
        return nArray;
    }

    /*
     * Enabled force condition propagation
     * Lifted jumps to return sites
     */
    public static int a(f f2) {
        int n = -1;
        switch (f2.g[1]) {
            case 0: {
                return 499;
            }
            case 4: {
                return 210;
            }
            case 9: {
                return 356;
            }
        }
        return n;
    }

    /*
     * Enabled force condition propagation
     * Lifted jumps to return sites
     */
    private static int f(f f2) {
        int n = -1;
        switch (f2.g[1]) {
            case 0: {
                return 500;
            }
            case 4: {
                return 211;
            }
            case 9: {
                return 358;
            }
        }
        return n;
    }

    public static void d(f f2) {
        block1: {
            int n;
            block2: {
                f f3;
                block0: {
                    if (a != 10 && a != 11 || g.j == null) break block0;
                    if (g.j.a.b <= f2.a.b) break block1;
                    f.u(g.j);
                    f3 = f2;
                    n = g.j.M - 1;
                    break block2;
                }
                f3 = f2;
                n = (f2.a.b() << 8) + f2.a.a();
            }
            f3.M = n;
        }
    }

    private static void a(int n, int[] nArray, int n2, int n3) {
        block10: {
            block9: {
                if (nArray[0] != 1) break block9;
                switch (n) {
                    case 20: {
                        f.a(nArray, n2, n3);
                        break block10;
                    }
                    case 21: {
                        f.e(nArray);
                        break block10;
                    }
                    case 22: {
                        f.b(nArray, n2, n3);
                        break block10;
                    }
                    case 23: {
                        f.d(nArray, n2, n3);
                        break block10;
                    }
                    case 24: {
                        f.f(nArray);
                        break block10;
                    }
                    case 25: {
                        f.e(nArray, n2, n3);
                    }
                    default: {
                        return;
                    }
                }
            }
            if (n == 22) {
                f.c(nArray, n2, n3);
            }
        }
    }

    public static boolean b(f f2) {
        return f2.L == 20 && f2.g[0] == 1 && f2.g[1] == 1;
    }

    public static void a(int[] nArray) {
        if (nArray[7] == 1) {
            nArray[12] = 0;
        }
    }

    private static void a(int[] nArray, int n, int n2) {
        int n3 = g.c.a.a() - 8;
        int n4 = g.c.a.b() - 8;
        boolean bl = g.a(n3, n4, 16, 16, n, n2, nArray[2], nArray[3]);
        boolean bl2 = nArray[1] == 0;
        if (bl2 && bl) {
            y = nArray[13];
            g.b(nArray[6]);
            if (nArray[4] > 0) {
                nArray[4] = nArray[4] - 1;
                if (nArray[4] == 0) {
                    nArray[0] = 0;
                }
            }
        }
        int n5 = nArray[1] = bl ? 1 : 0;
        if (nArray[0] == 1 && nArray[7] == 1) {
            nArray[12] = g.c % 6 < 3 ? 1 : 0;
        }
    }

    public static void a(Graphics graphics, int[] nArray, int n, int n2) {
        if (nArray[0] == 1 && nArray[7] == 1 && nArray[12] == 1) {
            graphics.setColor(nArray[8], nArray[9], nArray[10]);
            graphics.fillRect(n, n2, nArray[2], nArray[3]);
        }
    }

    private static void e(int[] nArray) {
        if (g.b == 0) {
            nArray[7] = nArray[7] + (int)g.d;
            z = nArray[7];
            if (nArray[7] >= nArray[8]) {
                z = -1;
                nArray[0] = 0;
                f.b(nArray);
                if (nArray[4] >= 0) {
                    g.b(nArray[4]);
                }
            }
        }
    }

    private static boolean a(int[] nArray) {
        if (nArray[0] == 1 && (nArray[5] == 1 || nArray[6] == 1)) {
            g.a();
            g.a(18, -1);
            e = true;
            return true;
        }
        return false;
    }

    public static void b(int[] nArray) {
        if (nArray[0] == 1) {
            nArray[7] = 0;
            if (z != -1) {
                nArray[7] = z;
            }
            nArray[8] = nArray[1] * 1000;
            if (nArray[2] > 0) {
                nArray[8] = nArray[8] + g.a() % nArray[2];
            }
            f.a(nArray);
            return;
        }
        if (g.a == 6) {
            z = -1;
        }
        nArray[7] = 0;
        if (nArray[6] == 1 || nArray[5] == 1) {
            g.c(g.a(2));
            e = false;
        }
    }

    public static void a(Graphics graphics, int[] nArray) {
        int n;
        if (nArray[0] == 1 && nArray[5] == 1 && (n = nArray[8] - nArray[7]) >= 0) {
            int n2 = n / 1000;
            int n3 = (n - n2 * 1000) / 10;
            int n4 = n2 / 60;
            int n5 = n2 - 60 * (n2 / 60);
            g.b(0, 0);
            g.b(1, 0);
            g.b(2, 0);
            g.b(3, 0);
            g.b(4, 0);
            g.b(5, 0);
            g.a(g.b, null, 0, 11, 0, 240, 320, 0);
            g.b(0, n4 / 10);
            g.b(1, n4 - n4 / 10 * 10);
            g.b(2, n5 / 10);
            g.b(3, n5 - n5 / 10 * 10);
            g.b(4, n3 / 10);
            g.b(5, n3 - n3 / 10 * 10);
            graphics.setColor(0xFF0000);
            byte[] byArray = g.a[12].a(15, 0);
            int n6 = byArray[0] & 0xFF;
            int n7 = byArray[1] & 0xFF;
            int n8 = byArray[2] & 0xFF;
            int n9 = byArray[3] & 0xFF;
            graphics.fillRect(n6, n7, n8, n9);
            g.b[0].a(0);
            g.a(graphics, g.b, null, 0, 11, 0, n6 + 10, n7 + 1, 4);
        }
    }

    private static void b(int[] nArray, int n, int n2) {
        int n3 = g.c.a.a() - 8;
        int n4 = g.c.a.b() - 8;
        boolean bl = g.a(n3, n4, 16, 16, n + nArray[11], n2 + nArray[12], nArray[13], nArray[14]);
        boolean bl2 = nArray[1] == 0;
        if (bl2 && bl) {
            f.a(0, g.c);
            int n5 = nArray[8];
            int n6 = nArray[10];
            int n7 = nArray[9];
            if (g.g[n5][n7][n6].L == 22) {
                int n8 = g.by;
                int n9 = g.bz;
                g.a(n5, n7, n6);
                g.a(n8, n9, false);
                g.b(n8, n9, false);
            }
        }
        nArray[1] = bl ? 1 : 0;
        f.c(nArray, n, n2);
    }

    private static void c(int[] nArray, int n, int n2) {
        boolean bl;
        boolean bl2 = nArray[0] == 1;
        if ((bl2 || nArray[10] == -1) && (bl = g.a(g.T >> 14, g.U >> 14, 240, 320, n, n2, nArray[2], nArray[3]))) {
            g.a(true);
        }
    }

    public static void a(Graphics graphics, int[] nArray, int n, int n2, boolean bl) {
        int n3 = g.c.a.a() - 8;
        int n4 = g.c.a.b() - 8;
        boolean bl2 = g.a(n3, n4, 16, 16, n, n2, nArray[2], nArray[3]);
        if (bl && bl2 && g.aT == 0) {
            g.a(graphics, 0, 46, 240, g.b[0].a() + 4);
            g.a(graphics, g.b, null, nArray[15], nArray[16], 0, 120, 48, 17);
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void b(Graphics var0, int[] var1_1, int var2_2, int var3_3) {
        block6: {
            if (var1_1[0] != 1 && var1_1[10] != -1 || !(var4_4 = g.a(0, 0, 240, 320, var2_2, var3_3, var1_1[2], var1_1[3])) || var1_1[13] <= 0 || var1_1[14] <= 0) break block6;
            var5_5 = 0;
            var6_6 = 0;
            var7_7 = 0;
            var8_8 = 0;
            var9_9 = g.a(g.a[15], 37);
            var10_10 = var9_9[2] - var9_9[0];
            var11_11 = var9_9[3] - var9_9[1];
            var12_12 = 0;
            switch (var1_1[4]) {
                case 0: {
                    var5_5 = var2_2 + var1_1[11];
                    var7_7 = var5_5 + var1_1[13];
                    var6_6 = var8_8 = var3_3 + var1_1[12];
                    v0 = var1_1[13];
                    v1 = var10_10;
                    ** GOTO lbl39
                }
                case 1: {
                    var5_5 = var2_2 + var1_1[11];
                    var7_7 = var5_5 + var1_1[13];
                    var6_6 = var8_8 = var3_3 + var1_1[12] + var1_1[14];
                    v0 = var1_1[13];
                    v1 = var10_10;
                    ** GOTO lbl39
                }
                case 2: {
                    v2 = var2_2;
                    v3 = var1_1;
                    v4 = 11;
                    ** GOTO lbl34
                }
                case 3: {
                    v2 = var2_2 + var1_1[11];
                    v3 = var1_1;
                    v4 = 13;
lbl34:
                    // 2 sources

                    var5_5 = var7_7 = v2 + v3[v4];
                    var6_6 = var3_3 + var1_1[12];
                    var8_8 = var6_6 + var1_1[14];
                    v0 = var1_1[14];
                    v1 = var11_11;
lbl39:
                    // 3 sources

                    var12_12 = v0 / v1;
                }
            }
            g.e(8);
            g.a(var0, g.a[15], 37, var5_5, var6_6, var7_7, var8_8, var12_12);
            g.f(8);
        }
    }

    public static int[] a(int[] nArray) {
        int[] nArray2 = new int[nArray.length + 1];
        System.arraycopy((Object)nArray, (int)0, (Object)nArray2, (int)0, (int)nArray.length);
        nArray2[12] = 1;
        return nArray2;
    }

    private static boolean a(int[] nArray, int n, int n2) {
        int n3 = g.b(n);
        int n4 = g.b(n2);
        int n5 = g.b(nArray[2]) + (nArray[2] % 16 == 0 ? 0 : 1);
        int n6 = g.b(nArray[3]) + (nArray[3] % 16 == 0 ? 0 : 1);
        for (int i = 0; i < n5; ++i) {
            for (int j = 0; j < n6; ++j) {
                if (!g.b(n3 + i, n4 + j, 4)) continue;
                return true;
            }
        }
        return false;
    }

    public static boolean c(f f2) {
        int[] nArray = g.g[g.by][g.bz][f2.g[8]].g;
        if (g.g[g.by][g.bz][f2.g[8]].g[0] == 1 && nArray[11] == 0) {
            int n;
            int n2 = f2.a.a();
            f f3 = f.a(n2, n = f2.a.b(), nArray[2], nArray[3]);
            boolean bl = f3 != null;
            boolean bl2 = true;
            if (a == 6 || a == 7 || a == 8 || a == 100 || a == 101 || a == 17) {
                bl2 = false;
            }
            if (!bl && bl2) {
                return !f.a(nArray, n2, n);
            }
        }
        return false;
    }

    public static void a(f f2, int n, int n2) {
        int[] nArray = f2.g;
        if (f2.g[12] == 0) {
            nArray[12] = 1;
            f.a(nArray, 7, false, false, n, n2, false);
        }
    }

    private static void A(f f2) {
        boolean bl;
        boolean bl2;
        int n;
        int[] nArray;
        int[] nArray2 = f2.g;
        if (f2.g[12] == 1) {
            nArray2[12] = 0;
            nArray = nArray2;
            n = 6;
            bl2 = false;
            bl = true;
        } else {
            nArray2[12] = 1;
            nArray = nArray2;
            n = 7;
            bl2 = false;
            bl = false;
        }
        f.a(nArray, n, bl2, bl, g.by, g.bz, true);
    }

    public static f a(int n, int n2, int[] nArray, int n3) {
        int n4;
        int n5;
        int[] nArray2;
        int[] nArray3 = new int[9];
        int[] nArray4 = nArray3;
        nArray3[0] = nArray[4];
        nArray4[1] = nArray[5];
        nArray4[8] = n3;
        if (nArray[0] == 1) {
            nArray4[2] = 0;
            nArray2 = nArray4;
            n5 = 3;
            n4 = 0;
        } else {
            nArray4[2] = g.b(nArray[2]) + (nArray[2] % 16 == 0 ? 0 : 1);
            nArray2 = nArray4;
            n5 = 3;
            n4 = g.b(nArray[3]) + (nArray[3] % 16 == 0 ? 0 : 1);
        }
        nArray2[n5] = n4;
        nArray4[4] = -1;
        nArray4[5] = nArray[7];
        nArray4[6] = 0;
        return new f(-1, 10, n, n2, nArray4);
    }

    private static f a(int n, int n2, int n3, int n4) {
        int n5 = g.b(n);
        int n6 = g.b(n2);
        int n7 = g.b(n3);
        int n8 = g.b(n4);
        for (int i = 0; i < n7; ++i) {
            for (int j = 0; j < n8; ++j) {
                f f2 = g.a(n5 + i, n6 + j);
                if (f2 == null || f2.L >= 9) continue;
                return f2;
            }
        }
        return null;
    }

    private static void d(int[] nArray, int n, int n2) {
        block8: {
            int n3;
            int[] nArray2;
            block10: {
                block9: {
                    if (nArray[12] != 1 || f.a(nArray, n, n2)) break block8;
                    f f2 = f.a(n, n2, nArray[2], nArray[3]);
                    boolean bl = f2 != null;
                    boolean bl2 = nArray[1] == 0;
                    if (bl2 && bl && (nArray[8] == 0 || 0 >= nArray[9])) {
                        f.a(nArray, 6, false, true, g.by, g.bz, true);
                    } else {
                        int n4;
                        int n5;
                        int[] nArray3;
                        f.a(nArray, 7, false, false, g.by, g.bz, true);
                        if (bl2 && bl && nArray[8] == 1 && 0 < nArray[9]) {
                            f.a(0, g.c);
                            g.b(nArray[10]);
                            nArray3 = nArray;
                            n5 = 1;
                            n4 = 1;
                        } else if (!bl) {
                            nArray3 = nArray;
                            n5 = 1;
                            n4 = nArray3[n5] = 0;
                        }
                    }
                    if (nArray[8] != 1 || 0 >= nArray[9]) break block9;
                    nArray2 = nArray;
                    n3 = 1;
                    break block10;
                }
                if (nArray[5] != 1) break block8;
                nArray2 = nArray;
                n3 = 0;
            }
            f.a(nArray2, n3, g.by, g.bz);
        }
    }

    public static void c(int[] nArray) {
        f.a(nArray, 7, true, false, g.by, g.bz, false);
        nArray[5] = 1;
        nArray[12] = 1;
    }

    public static void b(f f2, int n, int n2) {
        int[] nArray = f2.g;
        f f3 = g.a[n][n2][nArray[4]];
        if (g.by == n && g.bz == n2) {
            int n3 = f3.g[2];
            int n4 = f3.g[3];
            f3.g[2] = g.b(nArray[2]) + (nArray[2] % 16 == 0 ? 0 : 1);
            f3.g[3] = g.b(nArray[3]) + (nArray[3] % 16 == 0 ? 0 : 1);
            g.d(f3);
            g.a(f3, 192);
            f3.a.a = f2.a.a;
            f3.a.b = f2.a.b;
            g.b(f3, 192, false);
            f3.g[2] = n3;
            f3.g[3] = n4;
            f.a(f2.g, f2.g[5], n, n2);
            return;
        }
        f3.a.a = f2.a.a;
        f3.a.b = f2.a.b;
    }

    private static void a(int[] nArray, int n, boolean bl, boolean bl2, int n2, int n3, boolean bl3) {
        f f2 = g.a[n2][n3][nArray[4]];
        if (f2.a.d != nArray[n]) {
            f2.a.a(nArray[n], 0);
            if (bl3 && !g.A && nArray[11] != 1) {
                g.b(5);
            }
        }
        int n4 = f2.g[2];
        int n5 = f2.g[3];
        f2.g[2] = g.b(nArray[2]) + (nArray[2] % 16 == 0 ? 0 : 1);
        f2.g[3] = g.b(nArray[3]) + (nArray[3] % 16 == 0 ? 0 : 1);
        if (bl2) {
            g.a(f2, 192);
        } else {
            g.b(f2, 192, false);
        }
        f2.g[2] = n4;
        f2.g[3] = n5;
        if (bl) {
            g.a(f2.a);
        }
    }

    /*
     * Unable to fully structure code
     */
    public static void a(int[] var0, int var1_1, int var2_2, int var3_3) {
        block3: {
            var4_4 = g.a[var2_2][var3_3][var0[4]];
            var0[5] = var1_1;
            if (var2_2 != g.by || var3_3 != g.bz) break block3;
            if (var0[5] == 1) {
                var4_4.g[2] = g.b(var0[2]) + (var0[2] % 16 == 0 ? 0 : 1);
                var4_4.g[3] = g.b(var0[3]) + (var0[3] % 16 == 0 ? 0 : 1);
                g.a(var4_4, true);
                return;
            }
            g.d(var4_4);
            ** GOTO lbl-1000
        }
        if (var0[5] == 1) {
            var4_4.g[2] = g.b(var0[2]) + (var0[2] % 16 == 0 ? 0 : 1);
            v0 = var4_4.g;
            v1 = 3;
            v2 = g.b(var0[3]) + (var0[3] % 16 == 0 ? 0 : 1);
        } else lbl-1000:
        // 2 sources

        {
            var4_4.g[2] = 0;
            v0 = var4_4.g;
            v1 = 3;
            v2 = 0;
        }
        v0[v1] = v2;
    }

    private static void f(int[] nArray) {
        if (nArray[0] == 1 && g.b == 0) {
            boolean bl = true;
            if (nArray[3] == 1) {
                bl = g.c(1, -1, -1, -1, nArray[4], nArray[5], nArray[6], 0);
            }
            if (bl) {
                g.b(nArray[2]);
            }
        }
    }

    public static int[] b(int[] nArray) {
        int[] nArray2 = new int[nArray.length + 1];
        System.arraycopy((Object)nArray, (int)0, (Object)nArray2, (int)0, (int)nArray.length);
        nArray2[14] = 0;
        return nArray2;
    }

    public static void a(int[] nArray, int n, int n2, boolean bl, boolean bl2) {
        if (bl2) {
            int n3 = g.b(n + nArray[4]);
            int n4 = g.b(n2 + nArray[5]);
            int n5 = g.b(nArray[6]);
            int n6 = g.b(nArray[7]);
            g.a(n3, n4, n5, n6, 16);
            g.a(n3 - 1, n4 - 1, n5 + 2, n6 + 2);
        }
        if (nArray[0] == 1) {
            if (nArray[11] == 1) {
                g.c.g[11] = 0;
                nArray[10] = g.f[nArray[12]][nArray[13]].length;
                g.a(1, 0, nArray[14], nArray[10], 0, 33);
                f = nArray;
                return;
            }
            g.a(0, 0, nArray[14], nArray[10], 0, 33);
            return;
        }
        g.h(0);
        g.h(1);
        f = null;
        if (bl && nArray[11] == 1) {
            g.c.g[11] = nArray[14];
            g.bR = nArray[9];
        }
    }

    private static void e(int[] nArray, int n, int n2) {
        int n3 = g.c.a.a() - 8;
        int n4 = g.c.a.b() - 8;
        boolean bl = g.a(n3, n4, 16, 16, n, n2, nArray[2], nArray[3]);
        boolean bl2 = nArray[1] == 0;
        if (bl2 && bl) {
            int n5 = g.b(n + nArray[4]);
            int n6 = g.b(n2 + nArray[5]);
            int n7 = g.b(nArray[6]);
            int n8 = g.b(nArray[7]);
            for (int i = 0; i < n7; ++i) {
                for (int j = 0; j < n8; ++j) {
                    f f2 = g.a(n5 + i, n6 + j);
                    if (f2 == null || f2.L != 1 || !f.A(f2)) continue;
                    nArray[14] = nArray[14] + 1;
                    f2.g[17] = 1;
                    f.n(f2, 8);
                }
            }
        }
        g.c(nArray[11] == 1 ? 1 : 0, nArray[14]);
        if (nArray[14] >= nArray[10]) {
            if (nArray[11] == 1) {
                g.c.g[11] = nArray[14];
            }
            nArray[1] = 1;
            g.b(nArray[9]);
            nArray[0] = 0;
            g.h(0);
            g.h(1);
            f = null;
        }
    }

    public static void c() {
        a = new c[20];
        for (int i = 0; i < 20; ++i) {
            f.a[i] = new c(null, 0, 0, null);
        }
    }

    private static void b(f f2, int n, int n2, int n3) {
        f.a(f2, n, n2, n3, false, 0);
    }

    /*
     * Unable to fully structure code
     */
    private static void a(f var0, int var1_1, int var2_2, int var3_3, boolean var4_4, int var5_5) {
        block8: {
            var6_6 = -1;
            for (var7_7 = 0; var7_7 < 4; ++var7_7) {
                v0 = (byte)g.a(var0.g[21], 255 << var7_7 * 8);
                var8_8 = v0;
                if (v0 != -1) continue;
                var6_6 = var7_7;
                break;
            }
            if (var6_6 < 0) break block8;
            var7_7 = -1;
            for (var8_8 = 0; var8_8 < f.a.length; ++var8_8) {
                if (f.a[var8_8].a != null) continue;
                var7_7 = var8_8;
                break;
            }
            if (var7_7 < 0) break block8;
            var0.g[21] = g.a(var0.g[21], 255 << var6_6 * 8, var7_7);
            var8_9 = f.a[var7_7];
            var8_9.a(g.a[14]);
            var8_9.a = var0.a.a + (var1_1 << 14);
            var8_9.b = var0.a.b + (var2_2 << 14);
            var0.g[16] = var0.g[16] & -3;
            switch (var4_4 != false ? var5_5 : g.cu) {
                case 1: 
                case 2: 
                case 3: {
                    v1 = var8_9;
                    v2 = 0;
                    ** GOTO lbl37
                }
                case 5: 
                case 6: 
                case 7: {
                    var8_9.b(1 + var3_3);
                    var0.g[16] = var0.g[16] | 2;
                    break;
                }
                case 4: {
                    v1 = var8_9;
                    v2 = 2;
                    ** GOTO lbl37
                }
                case 0: {
                    v1 = var8_9;
                    v2 = 3;
lbl37:
                    // 3 sources

                    v1.b(v2 + var3_3);
                }
            }
            var0.g[16] = var0.g[16] | 1;
        }
    }

    private static void c(Graphics graphics, f f2, boolean bl) {
        if ((f2.g[16] & 1) != 0 && (bl && (f2.g[16] & 2) != 0 || !bl && (f2.g[16] & 2) == 0)) {
            for (int i = 0; i < 4; ++i) {
                byte by = (byte)g.a(f2.g[21], 255 << i * 8);
                if (by < 0) continue;
                c c2 = a[by];
                c2.a -= g.T;
                c2.b -= g.U;
                c2.a(graphics);
                c2.a += g.T;
                c2.b += g.U;
            }
        }
    }

    public static void e(f f2) {
        int n = 0;
        for (int i = 0; i < 4; ++i) {
            byte by = (byte)g.a(f2.g[21], 255 << i * 8);
            if (by < 0) continue;
            c c2 = a[by];
            c2.a();
            if (c2.a()) {
                f2.g[21] = g.a(f2.g[21], 255 << i * 8, -1);
                c2.a((a)null);
                continue;
            }
            ++n;
        }
        if (n == 0) {
            f2.g[16] = f2.g[16] & 0xFFFFFFFE;
        }
    }

    public static void d() {
        b = new int[4];
    }

    private static void j() {
        f.b[0] = Integer.MAX_VALUE;
        f.b[1] = Integer.MAX_VALUE;
        f.b[2] = -2147483647;
        f.b[3] = -2147483647;
    }

    private static boolean f() {
        return b[0] > b[2] || b[1] > b[3];
    }

    private static void a(int n, int n2, int n3, int n4) {
        if (n < b[0]) {
            f.b[0] = n;
        }
        if (n2 < b[1]) {
            f.b[1] = n2;
        }
        if (n3 > b[2]) {
            f.b[2] = n3;
        }
        if (n4 > b[3]) {
            f.b[3] = n4;
        }
    }

    private static void B(f f2) {
        if ((f2.g[12] < 100 || (f2.g[16] & 0x20) == 0) && f2.g[22] < 0) {
            int n;
            int[] nArray;
            int n2;
            if (f2.g[23] <= 0) {
                if (!f.p(f2)) {
                    f2.g[22] = g.a(f2, f2.a.a() << 14, f2.a.b() << 14, 1, 1, 70, -1);
                    n2 = 16;
                    nArray = f2.g;
                    n = f2.g[16] | 0x20;
                }
            } else {
                n2 = 23;
                nArray = f2.g;
                n = nArray[n2] = f2.g[23] - (int)g.d;
            }
        }
        if ((f2.g[12] >= 100 || (f2.g[16] & 0x20) == 0) && f2.g[22] >= 0) {
            g.a(f2.g[22], true, 0, true, -128);
            g.k(f2.g[22]);
        }
        if (f2.g[22] >= 0 && f2.g[12] < 100) {
            g.c(f2.g[22], f2.a.a() << 14, f2.a.b() << 14);
        }
    }

    public static boolean d(f f2) {
        int n = g.h(f2.g[0], 10);
        return (n == 5 || n == 7) && (f2.g[16] & 0x20) != 0;
    }

    private static boolean p(f f2) {
        boolean bl = false;
        int[] nArray = f2.a.a();
        int[] nArray2 = null;
        bl = false | g.d(f2.a.a() / 16, f2.a.b() / 16);
        if (g.ao && !bl) {
            int[] nArray3 = g.d.a();
            nArray2 = nArray3;
            nArray3[0] = nArray3[0] + (g.T >> 14);
            nArray2[1] = nArray2[1] + (g.U >> 14);
            nArray2[2] = nArray2[2] + (g.T >> 14);
            nArray2[3] = nArray2[3] + (g.U >> 14);
            bl = g.a(nArray[0], nArray[1], nArray[2] - nArray[0], nArray[3] - nArray[1], nArray2[0], nArray2[1], nArray2[2] - nArray2[0], nArray2[3] - nArray2[1], 55);
        }
        for (int i = 0; i < g.cg && !bl; ++i) {
            f f3 = g.e[i];
            if (f3.L != 15) continue;
            nArray2 = f3.a.a();
            bl = g.a(nArray[0], nArray[1], nArray[2] - nArray[0], nArray[3] - nArray[1], nArray2[0], nArray2[1], nArray2[2] - nArray2[0], nArray2[3] - nArray2[1], 55);
        }
        if (g.d() && !bl && !g.a(g.c.a.a, g.c.a.b, f2.a.a, f2.a.b, null, false, 129)) {
            g.a(c);
            bl = g.a(nArray[0], nArray[1], nArray[2] - nArray[0], nArray[3] - nArray[1], c[0], c[1], c[2] - c[0], c[3] - c[1], 55);
        }
        return bl;
    }

    private static void C(f f2) {
        int n = g.h(f2.g[0], 10);
        if ((n == 5 || n == 7) && f2.g[12] != -1) {
            if (f2.g[12] < 100 && f.p(f2) && (f2.g[16] & 0x20) != 0) {
                f2.g[16] = f2.g[16] & 0xFFFFFFDF;
            }
            f.B(f2);
        }
    }

    private static void D(f f2) {
        if ((f2.g[12] < 100 || (f2.g[16] & 0x20) == 0) && f2.g[22] < 0 && f2.g[23] > 0) {
            f2.g[23] = 0;
        }
    }

    public static void f(f f2) {
        int n;
        int n2;
        int[] nArray;
        f2.g[22] = -1;
        if ((f2.g[16] & 0x20) == 0) {
            nArray = f2.g;
            n2 = 23;
            n = 10000;
        } else {
            nArray = f2.g;
            n2 = 23;
            n = 0;
        }
        nArray[n2] = n;
        f2.g[16] = f2.g[16] & 0xFFFFFFDF;
    }

    private static void d(Graphics graphics, f f2, boolean bl) {
        int n = g.h(f2.g[0], 10);
        if ((n == 5 || n == 7) && f2.g[12] != -1 && f2.g[22] >= 0) {
            a a2 = f2.a.a;
            int n2 = a2.b(f2.a.d, 0);
            int n3 = a2.b(n2);
            int n4 = g.a(a2, f2.a.d, 0);
            int n5 = a2.h[f2.a.d] + 0;
            int n6 = 0;
            for (int i = 0; i < n3; ++i) {
                int n7 = a2.e[n2] + i;
                int n8 = a2.d[n7] & 0xFF;
                int n9 = a2.c[n7] & 0xFF;
                if (a2.k[n9 |= (n8 & 0xC0) << 2] != 1) continue;
                a2.b(c, n2, i, 0, 0, n4);
                c[0] = c[0] + a2.i[n5];
                c[2] = c[2] + a2.i[n5];
                c[1] = c[1] + a2.j[n5];
                c[3] = c[3] + a2.j[n5];
                if (n6 % 2 == 0 && bl || n6 % 2 == 1 && !bl) {
                    g.a(graphics, f2.g[22], c[0] << 14, c[1] << 14, g.r);
                    f.a(g.r[0], g.r[1], g.r[2], g.r[3]);
                }
                ++n6;
            }
        }
    }

    public static void a(Graphics graphics, f f2) {
        int n = g.h(f2.g[0], 10);
        if ((n == 5 || n == 7) && f2.g[12] != -1 && f2.g[12] != 101 && (f2.g[16] & 0x20) != 0) {
            int n2;
            int n3;
            if (f.u(f2)) {
                int[] nArray = f.b(f2, true, false);
                n3 = nArray[0] >> 14;
                n2 = nArray[1];
            } else {
                n3 = f2.a.a - g.T >> 14;
                n2 = f2.a.b - g.U;
            }
            int n4 = n2 >> 14;
            a a2 = f2.a.a;
            f2.a.a.e = f2.g[1];
            a2.a(f2.g[2]);
            int n5 = a2.b(f2.a.d, f2.a.e);
            int n6 = a2.b(n5);
            int n7 = g.a(a2, f2.a.d, f2.a.e);
            int n8 = a2.h[f2.a.d] + f2.a.e;
            boolean bl = false;
            for (int i = 0; i < n6; ++i) {
                int n9 = a2.e[n5] + i;
                int n10 = a2.d[n9] & 0xFF;
                int n11 = a2.c[n9] & 0xFF;
                int n12 = a2.e[n11 |= (n10 & 0xC0) << 2];
                if (bl) {
                    a2.b(c, n5, i, 0, 0, n7);
                    c[0] = c[0] + (n3 + a2.i[n8]);
                    c[2] = c[2] + (n3 + a2.i[n8]);
                    c[1] = c[1] + (n4 + a2.j[n8]);
                    c[3] = c[3] + (n4 + a2.j[n8]);
                    g.a(graphics, f2.a.a(), f2.a.b(), c[0] + (c[2] - c[0] >> 1), c[1] + (c[3] - c[1] >> 1), a2, 655, 0);
                    return;
                }
                if (a2.k[n11] != 1 || n12 != 1) continue;
                bl = true;
            }
        }
    }

    public static void e() {
        a = new byte[10][3];
        for (int i = 0; i < a.length; ++i) {
            for (int j = 0; j < a[i].length; ++j) {
                f.a[i][j] = -1;
            }
        }
    }

    private static int b() {
        int n;
        for (n = 0; n < a.length; ++n) {
            if (a[n][0] != -1) continue;
            return n;
        }
        byte[][] byArray = new byte[a.length + 1][3];
        System.arraycopy((Object)a, (int)0, (Object)byArray, (int)0, (int)a.length);
        int n2 = a.length;
        a = byArray;
        for (n = 0; n < a[n2].length; ++n) {
            f.a[n2][n] = -1;
        }
        return n2;
    }

    private static int a(f f2, int n, int n2) {
        int n3 = f2.g[30 + n];
        return a[n3][n2];
    }

    private static void c(f f2, int n, int n2, int n3) {
        int n4 = f2.g[30 + n];
        f.a[n4][n2] = (byte)n3;
    }

    private static void b(int n) {
        for (int i = 0; i < a[n].length; ++i) {
            f.a[n][i] = -1;
        }
    }

    private static int a(int[] nArray) {
        int n = 0;
        int n2 = g.h(nArray[0], 33);
        for (int i = 0; i < n2; ++i) {
            int n3 = g.d(nArray[0], i, 11);
            if (n3 == 0) {
                n |= g.d(nArray[0], i, 7);
                continue;
            }
            for (int j = 0; j < n3; ++j) {
                n |= g.d(nArray[0], i, j, 1);
            }
        }
        return n;
    }

    private static void g(int[] nArray) {
        int n = g.h(nArray[0], 33);
        for (int i = 0; i < n; ++i) {
            int n2 = g.d(nArray[0], i, 11);
            if (n2 == 0) {
                nArray[30 + i] = g.d(nArray[0], i, 0);
                continue;
            }
            nArray[30 + i] = f.b();
            for (int j = 0; j < n2; ++j) {
                f.a[nArray[30 + i]][j] = (byte)g.d(nArray[0], i, j, 0);
            }
        }
        nArray[18] = f.a(nArray);
    }

    public static int[] c(int[] nArray) {
        int n;
        int n2;
        int[] nArray2;
        int n3;
        if (a == null) {
            a = new int[g.d()];
        }
        int[] nArray3 = null;
        if (nArray != null) {
            nArray3 = new int[nArray.length + 16 + g.d()];
            System.arraycopy((Object)nArray, (int)0, (Object)nArray3, (int)0, (int)nArray.length);
            nArray3[0] = g.a(g.m, nArray3[0]);
        } else {
            nArray3 = new int[30 + g.d()];
        }
        for (n3 = 0; n3 < 16; ++n3) {
            nArray3[12 + n3] = 0;
        }
        for (n3 = 0; n3 < 4; ++n3) {
            nArray3[21] = g.a(nArray3[21], 255 << n3 * 8, -1);
        }
        int n4 = g.h(nArray3[0], 10);
        if (n4 == 5 || n4 == 7) {
            nArray3[23] = -1;
        }
        nArray3[22] = -1;
        if (nArray == null) {
            nArray2 = nArray3;
            n2 = 12;
            n = -1;
        } else {
            nArray2 = nArray3;
            n2 = 12;
            n = 0;
        }
        nArray2[n2] = n;
        f.g(nArray3);
        return nArray3;
    }

    public static void g(f f2) {
        int n;
        int n2;
        int[] nArray;
        int n3;
        int n4;
        int n5;
        g.a(f2, 1, false);
        int n6 = g.h(f2.g[0], 10);
        if ((f2.g[16] & 0x800) == 0) {
            n5 = g.h(f2.g[0], 33);
            for (n4 = 0; n4 < n5; ++n4) {
                n3 = g.d(f2.g[0], n4, 11);
                if (n3 == 0) continue;
                f.b(f2.g[30 + n4]);
            }
            if (f2.g[9] >= 0) {
                g.b(f2.g[9]);
            }
            if (n6 == 0 || n6 == 3 || n6 == 5 || n6 == 7) {
                nArray = f2.g;
                n2 = 2;
                n = 2;
            }
        } else {
            n2 = 16;
            nArray = f2.g;
            n = nArray[n2] = f2.g[16] & 0xFFFFFFBF;
        }
        if ((f2.g[16] & 0x400) == 0 && g.a == 6 && g.b != 4) {
            n5 = g.h(f2.g[0], 26);
            n4 = 0;
            n3 = f2.a.a();
            int n7 = f2.a.b();
            if (n6 != 1) {
                int[] nArray2 = g.b(f2.a);
                n3 = nArray2[0] + (nArray2[2] - nArray2[0] >> 1);
                if (!g.b(n3 / 16, (n7 = nArray2[1]) / 16, 5)) {
                    n4 = 1;
                }
                if (n4 == 0 && g.a(g.s, nArray2[0] / 16, nArray2[1] / 16, nArray2[2] / 16, nArray2[3] / 16, 5)) {
                    n4 = 1;
                    n3 = g.s[0] * 16 + 8;
                    n7 = g.s[1] * 16 + 8;
                }
            } else {
                n4 = 1;
            }
            if (n4 != 0) {
                g.b(n5, n3 << 14, n7 << 14);
                f2.g[16] = f2.g[16] | 0x400;
            }
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void g(f var0, int var1_1) {
        g.i(null);
        var2_2 = f.a(var0.g);
        var3_3 = var0.g[0];
        var4_4 = g.h(var0.g[0], 33);
        var0.g[0] = var1_1;
        var0.g[18] = var5_5 = f.a(var0.g);
        for (var8_6 = 0; var8_6 < var4_4; ++var8_6) {
            var9_7 = g.d(var3_3, var8_6, 11);
            if (var9_7 == 0 || ((var10_8 = g.d(var3_3, var8_6, 7)) & var5_5) != 0) continue;
            f.b(var0.g[30 + var8_6]);
        }
        System.arraycopy((Object)var0.g, (int)30, (Object)f.a, (int)0, (int)g.d());
        var6_9 = g.h(var0.g[0], 33);
        for (var8_6 = 0; var8_6 < var6_9; ++var8_6) {
            block10: {
                block9: {
                    var9_7 = g.d(var0.g[0], var8_6, 11);
                    var10_8 = g.d(var0.g[0], var8_6, 7);
                    if ((var2_2 & var10_8) == 0) break block9;
                    var13_12 = g.h(var3_3, 33);
                    for (var14_13 = 0; var14_13 < var13_12; ++var14_13) {
                        var15_14 = g.d(var3_3, var14_13, 7);
                        if (var15_14 != var10_8) continue;
                        v0 = var0.g;
                        v1 = 30 + var8_6;
                        v2 = f.a[var14_13];
                        ** GOTO lbl37
                    }
                    break block10;
                }
                if (var9_7 != 0) {
                    var0.g[30 + var8_6] = f.b();
                    for (var13_12 = 0; var13_12 < var9_7; ++var13_12) {
                        f.a[var0.g[30 + var8_6]][var13_12] = (byte)g.d(var0.g[0], var8_6, var13_12, 0);
                    }
                } else {
                    v0 = var0.g;
                    v1 = 30 + var8_6;
                    v2 = g.d(var0.g[0], var8_6, 0);
lbl37:
                    // 2 sources

                    v0[v1] = v2;
                }
            }
            var11_10 = g.d(var0.g[0], var8_6, 5);
            var12_11 = g.d(var0.g[0], var8_6, 6);
            if (var9_7 > 0) {
                for (var13_12 = 0; var13_12 < var9_7; ++var13_12) {
                    if (f.c(var0, var8_6, var13_12) != 0 || var11_10 < 0 || var12_11 < 0) continue;
                    var0.g[18] = var0.g[18] & ~g.d(var0.g[0], var8_6, var13_12, 1);
                }
                continue;
            }
            if (f.c(var0, var8_6, -1) != 0 || var11_10 < 0 || var12_11 < 0) continue;
            var0.g[18] = var0.g[18] & ~var10_8;
        }
        var7_15 = g.i(var0.g[0], 34);
        if (var7_15 == -1) {
            var0.g[16] = var0.g[16] & -2049;
            var0.g[16] = var0.g[16] & -4097;
            var0.g[24] = 0;
        }
        g.e(var0);
        g.i(var0);
    }

    public static void h(f f2) {
        if (f2.L == 1) {
            int n;
            boolean bl;
            int n2 = f2.g[14];
            int n3 = f2.g[2];
            boolean bl2 = bl = f2.g[21] == 1;
            if (g.f[n2][n3] != -1) {
                n2 = g.f[n2][n3];
            }
            if (g.v[n3] != -1) {
                n3 = g.v[n3];
            }
            int n4 = f2.g[1];
            int n5 = f.d(f2);
            int n6 = f2.g[n5 + 11];
            int n7 = f2.g[n5 + 12];
            int n8 = f2.g[20];
            f2.L = 3;
            f2.g[0] = g.w[n4];
            f2.g[1] = n3;
            f2.g[2] = n2;
            f2.g[3] = -120;
            f2.g[4] = -120;
            f2.g[5] = 240;
            f2.g[6] = 240;
            f2.g[7] = 0;
            f2.g[8] = 0;
            f2.g[9] = -1;
            f2.g[10] = 0;
            f2.g[11] = 0;
            f2.g[9] = n8;
            for (n = 0; n < 16; ++n) {
                f2.g[12 + n] = 0;
            }
            for (n = 0; n < 4; ++n) {
                f2.g[21] = g.a(f2.g[21], 255 << n * 8, -1);
            }
            f2.g[13] = n6;
            f2.g[14] = n7;
            if (f2.g[13] == 0 && f2.g[14] == 0) {
                f2.g[13] = 0;
                f2.g[14] = 16384;
            }
            f2.g[12] = 23;
            f2.g[18] = f.a(f2.g);
            g.e(f2);
            f.g(f2.g);
            f.c(f2);
            f2.g[15] = 0;
            if (bl) {
                f2.g[16] = f2.g[16] | 0x8000;
            }
        }
    }

    public static void a(f f2, int n, int n2, int n3) {
        f2.g[0] = n;
        f.g(f2.g);
        f2.g[2] = n2;
        f2.g[1] = n3;
        f2.g[19] = 0;
        f2.g[16] = 0;
        f2.g[3] = -120;
        f2.g[4] = -120;
        f2.g[5] = 240;
        f2.g[6] = 240;
        f2.g[9] = -1;
        f2.g[12] = 4;
        g.e(f2);
        f.k(f2);
        f.c(f2);
    }

    private static void a(f f2, int n, int n2, boolean bl, int n3, int n4) {
        int n5 = g.h(f2.g[0], 10);
        int n6 = g.d(f2.g[0], n, 5);
        int n7 = g.d(f2.g[0], n, 6);
        if (n6 != -1 && n7 != -1) {
            int n8;
            int n9;
            int n10 = f2.a.a + (n3 << 14);
            int n11 = f2.a.b + (n4 << 14);
            int n12 = f2.a.a + (20 + (g.a() % 100 - 50) << 14);
            int n13 = f2.a.b + (20 + (g.a() % 100 - 50) << 14);
            if (g.a == 6 && g.b == 4 && g.cw == 0) {
                n12 += 0x500000;
            }
            int n14 = 819200;
            if (g.a == 6 && g.b == 4 && g.cw == 0) {
                n14 += g.cC;
            }
            int n15 = g.d(n10 - n12) * 1000 / n14;
            int n16 = g.d(n11 - n13) * 1000 / 819200;
            int n17 = g.d(n10 - n12) / (n15 + 1);
            int n18 = g.d(n11 - n13) / (n16 + 1);
            int n19 = f2.g[1];
            int n20 = n9 = f2.g[2];
            if (n5 == 0 || n5 == 3 || n5 == 5 || n5 == 7) {
                n20 = 2;
            }
            if (bl) {
                n8 = g.d(f2.g[0], n, 7);
                if (n2 >= 0) {
                    n8 = g.d(f2.g[0], n, n2, 1);
                }
                f2.g[18] = f2.g[18] & ~n8;
            }
            if (!g.N || n5 == 2) {
                n8 = g.d(f2.g[0], n, 8);
                g.a(f2.a.a, n6, n7, n10 >> 14, n11 >> 14, n17, n18, n12, n13, n19, n9, n8, n20);
            }
        }
    }

    private static void e(Graphics graphics, f f2, boolean bl) {
        int n;
        int n2;
        int n3;
        int n4;
        int n5;
        block18: {
            block19: {
                block16: {
                    block17: {
                        int n6;
                        int n7 = g.h(f2.g[0], 10);
                        f2.a.a.e = f2.g[1];
                        f2.a.a.a(f2.g[2]);
                        f.j();
                        switch (n7) {
                            case 0: 
                            case 3: 
                            case 5: 
                            case 7: {
                                f.d(f2, bl);
                            }
                        }
                        f.d(graphics, f2, true);
                        if (f2.g[10] != 5 && f2.g[12] < 100 && (n5 = !(n7 == 1 && f2.g[10] == 4 || f2.g[12] == 9 && (f2.g[12] != 9 || n7 != 4 && n7 != 6 || f2.g[12] == 103 || f2.g[12] == 104 || f2.g[12] == 17)) ? 1 : 0) != 0 && (n6 = g.h(f2.g[0], 22)) >= 0) {
                            f.a(graphics, n6, f2.a.a >> 14, f2.a.b >> 14);
                        }
                        switch (n7) {
                            case 0: 
                            case 3: 
                            case 5: 
                            case 7: {
                                break;
                            }
                            case 1: {
                                break;
                            }
                            case 2: {
                                f.O(f2);
                            }
                        }
                        f.c(graphics, f2, true);
                        g.e(32);
                        g.b(f2.g[18], true);
                        if ((f2.g[16] & 0x1000) == 0) break block16;
                        if (f2.g[12] != 106) break block17;
                        n4 = f2.g[26];
                        n3 = f.g(f2);
                        n2 = f2.g[25];
                        n = f.c(f2, 0);
                        break block18;
                    }
                    n4 = f2.g[25];
                    n3 = f.g(f2);
                    break block19;
                }
                n4 = 0;
                n3 = 0;
            }
            n2 = 0;
            n = 0;
        }
        g.b(n4, n3, n2, n);
        if (f2.g[12] != 101) {
            n5 = g.h(f2.g[0], 34);
            g.g(n5 != -1 ? g.i(f2.g[0], 14) : -1);
            if ((f2.g[16] & 0x10) != 0) {
                g.b(-1, -1, 15, -1, 9);
            } else if ((f2.g[16] & 8) != 0) {
                g.b(18, 1, 15, 18, -1);
            } else {
                g.b(-1, -1, -1, -1, -1);
            }
        } else {
            g.b(-1, -1, -1, -1, -1);
            g.g(-1);
        }
        f2.a.a(graphics);
        if ((g.ag & 0x20) != 0) {
            f.a(g.g(3, 11), g.g(3, 12), g.g(3, 13), g.g(3, 14));
        }
        g.f(32);
        f.c(graphics, f2, false);
        f.d(graphics, f2, false);
        f.d(graphics, f2);
    }

    private static void d(Graphics graphics, f f2) {
        if (g.g == 2) {
            a a2 = f2.a.a;
            int n = a2.b(f2.a.d, f2.a.e);
            int n2 = a2.b(n);
            int n3 = g.a(a2, f2.a.d, f2.a.e);
            int n4 = a2.h[f2.a.d] + f2.a.e;
            graphics.setColor(255);
            graphics.drawLine(f2.a.a() - 10, f2.a.b(), f2.a.a() + 10, f2.a.b());
            graphics.drawLine(f2.a.a(), f2.a.b() - 10, f2.a.a(), f2.a.b() + 10);
            graphics.setColor(0xFF0000);
            for (int i = 0; i < n2; ++i) {
                a2.b(c, n, i, 0, 0, n3);
                c[0] = c[0] + (f2.a.a() + a2.i[n4]);
                c[2] = c[2] + (f2.a.a() + a2.i[n4]);
                c[1] = c[1] + (f2.a.b() + a2.j[n4]);
                c[3] = c[3] + (f2.a.b() + a2.j[n4]);
                graphics.drawRect(c[0], c[1], c[2] - c[0], c[3] - c[1]);
            }
        }
    }

    public static void f() {
        int n;
        if (a != null) {
            for (n = 0; n < a.length; ++n) {
                f.a[n] = null;
            }
        }
        a = null;
        d = null;
        int n2 = 0;
        int n3 = 0;
        for (n = 0; n < g.T.length; ++n) {
            int n4 = g.m(n);
            n2 = Math.max((int)n2, (int)n4);
            int n5 = g.h(n, 33);
            int n6 = 0;
            for (int i = 0; i < n5; ++i) {
                int n7 = g.d(n, i, 11);
                if (n7 == 0) {
                    ++n6;
                    continue;
                }
                n6 += n7;
            }
            n3 = Math.max((int)n6, (int)n3);
        }
        a = new int[n2][4];
        d = new int[n3];
    }

    private static int a(f f2, int n, int n2, boolean bl) {
        int n3;
        int n4;
        a a2 = f2.a.a;
        int n5 = a2.b(f2.a.d, f2.a.e);
        int n6 = a2.b(n5);
        int n7 = f2.g[18];
        if (bl) {
            n4 = g.a(a2, f2.a.d, f2.a.e);
            n3 = g.b(a2, f2.a.d, f2.a.e);
            int n8 = g.e(a2, f2.a.d, f2.a.e);
            B = 0;
            A = 0;
            for (int i = 0; i < n6; ++i) {
                int n9 = g.c(a2, n5, i);
                if (n9 == 1) {
                    f.d[f.B++] = g.d(a2, n5, i);
                    continue;
                }
                a2.b(a[A], n5, i, 0, 0, n4);
                int[] nArray = a[A];
                nArray[0] = nArray[0] + n3;
                int[] nArray2 = a[A];
                nArray2[2] = nArray2[2] + n3;
                int[] nArray3 = a[A];
                nArray3[1] = nArray3[1] + n8;
                int[] nArray4 = a[A];
                nArray4[3] = nArray4[3] + n8;
                ++A;
            }
        }
        int n10 = A - 1;
        int n11 = B - 1;
        if (A > 0 && B > 0) {
            for (n4 = n6 - 1; n4 >= 0; --n4) {
                n3 = g.c(a2, n5, n4);
                if (n3 == 1) {
                    --n11;
                    continue;
                }
                if (n11 < 0 || n10 < 0) continue;
                if ((d[n11] & n7) != 0 && g.a(a[n10][0], a[n10][1], a[n10][2], a[n10][3], n, n2)) {
                    return d[n11];
                }
                --n10;
            }
        }
        return 0;
    }

    private static int b(f f2, int n) {
        int n2 = g.h(f2.g[0], 33);
        for (int i = 0; i < n2; ++i) {
            int n3 = g.d(f2.g[0], i, 7);
            if ((n3 & n) == 0) continue;
            return i;
        }
        return -1;
    }

    private static int b(f f2, int n, int n2) {
        if (n >= 0) {
            int n3 = g.d(f2.g[0], n, 11);
            for (int i = 0; i < n3; ++i) {
                int n4 = g.d(f2.g[0], n, i, 1);
                if ((n4 & n2) == 0) continue;
                return i;
            }
        }
        return -1;
    }

    private static void d(f f2, int n, int n2, int n3) {
        int n4 = g.d(f2.g[0], n, 11);
        if (n4 == 0) {
            int n5 = 30 + n;
            f2.g[n5] = f2.g[n5] - n3;
            return;
        }
        if (n2 >= 0) {
            f.c(f2, n, n2, f.a(f2, n, n2) - n3);
        }
    }

    private static int b(f f2, boolean bl) {
        boolean bl2;
        f2.g[20] = g.a(f2.g[20], 255, 1);
        f2.g[20] = g.a(f2.g[20], 0xFFFF00, g.bt);
        int n = 4;
        boolean bl3 = bl2 = false;
        block0: while (!bl2) {
            int n2 = g.h(f2.g[0], 33);
            for (int i = 0; i < n2; ++i) {
                int n3 = g.d(f2.g[0], i, 7);
                int n4 = g.d(f2.g[0], i, 1);
                int n5 = g.d(f2.g[0], i, 12);
                if ((n3 & f2.g[19]) == 0) {
                    if (f.c(f2, i, -1) == 0) {
                        f2.g[19] = f2.g[19] | n3;
                        if (n4 != -1) {
                            f.g(f2, n4);
                            continue block0;
                        }
                        f2.g[17] = i;
                        n = (f2.g[16] & 0x1000) == 0 || (f2.g[25] & n3) != 0 || n5 == -1 ? 100 : 106;
                        bl3 = true;
                        continue block0;
                    }
                } else if (n4 == -1) {
                    n = (f2.g[16] & 0x1000) == 0 ? 101 : 107;
                    bl3 = true;
                    continue block0;
                }
                if (i != n2 - 1) continue;
                bl2 = true;
            }
        }
        if ((f2.g[16] & 0x40) == 0 && n != 101) {
            if (bl) {
                f.c(f2, n);
            }
            if (n != 100 && n != 106) {
                f2.g[16] = f2.g[16] & 0xFFFFFDFF;
                f2.g[16] = f2.g[16] & 0xFFFFBFFF;
            }
        } else if (bl) {
            f.c(f2, 101);
        } else {
            n = 101;
        }
        return n;
    }

    public static void a(f f2, f f3) {
        f.E(f2);
        f.c(f2, 104);
        int n = f3.a.a + (f3.g[2] * 16 / 2 << 14);
        int n2 = f3.a.b + (f3.g[3] * 16 / 2 << 14);
        f.f(f2, n, n2, 0);
        int[] nArray = f2.a.a();
        f.a(f2, 0, -(nArray[3] - nArray[1]) / 2, 9, true, 0);
        g.b(14);
    }

    private static void E(f f2) {
        boolean bl = f.d(f2);
        if (f2.g[10] != 3 && f2.g[10] != 4 && f2.g[12] < 100 && f2.g[12] != 14 && !bl) {
            int n = g.h(f2.g[0], 33);
            for (int i = 0; i < n; ++i) {
                int n2;
                int n3 = g.d(f2.g[0], i, 11);
                if (n3 > 0) {
                    for (n2 = 0; n2 < n3; ++n2) {
                        int n4 = g.d(f2.g[0], i, n2, 0);
                        if (n4 <= 0) continue;
                        if (!d) {
                            n4 = 65;
                        }
                        f.a(f2, i, n2, n4, false, 0, 0, -1, true);
                    }
                    continue;
                }
                n2 = g.d(f2.g[0], i, 0);
                if (n2 <= 0) continue;
                if (!d) {
                    n2 = 65;
                }
                f.a(f2, i, -1, n2, false, 0, 0, -1, true);
            }
            f.i(f2);
            f.G(f2);
            f.f(f2, g.c.a.a, g.c.a.b, 0);
            f.c(f2, 103);
            return;
        }
        if (bl) {
            f2.g[16] = f2.g[16] & 0xFFFFFFDF;
        }
    }

    private static void a(f f2, int n, int n2, int n3, int n4) {
        int n5 = g.h(f2.g[0], 10);
        if (!f.d(f2) && !f.v(f2)) {
            f.i(f2);
            int n6 = g.h(f2.g[0], 33);
            int n7 = 0;
            int n8 = 0;
            if ((n5 == 0 || n5 == 3 || n5 == 3) && n2 >= (n -= n >> 2)) {
                f2.g[16] = f2.g[16] | 8;
            }
            while (n2 > 0 && n8 < n6) {
                int n9 = g.a() % n6;
                if ((n7 & 1 << n9) != 0) continue;
                int n10 = f.c(f2, n9, -1);
                if (n10 > 0) {
                    int n11 = g.d(f2.g[0], n9, 11);
                    if (n11 > 0) {
                        int n12;
                        int n13;
                        while ((n13 = f.c(f2, n9, n12 = g.a() % n11)) == 0) {
                        }
                        if (n13 > n2) {
                            n13 = n2;
                        }
                        f.a(f2, n9, n12, n13, false, 0, 0, -1, true);
                        n2 -= n13;
                        continue;
                    }
                    if (n10 > n2) {
                        n10 = n2;
                    }
                    f.a(f2, n9, -1, n10, false, 0, 0, -1, true);
                    n2 -= n10;
                    n7 |= 1 << n9;
                    ++n8;
                    continue;
                }
                n7 |= 1 << n9;
                ++n8;
            }
            f.c(f2, 103);
            f.f(f2, n3, n4, 0);
        }
    }

    private static void F(f f2) {
        block5: {
            int n;
            f f3;
            block6: {
                block4: {
                    f.b(f2, true);
                    if ((f2.g[16] & 0x1000) == 0) break block4;
                    if (f2.g[12] == 101 || f2.g[12] == 100 || f2.g[12] == 107) break block5;
                    if (f2.g[12] == 106) {
                        f.M(f2);
                        f2.g[25] = f2.g[25] | f2.g[26];
                        f2.g[26] = 0;
                        f3 = f2;
                        n = 107;
                    } else {
                        f3 = f2;
                        n = 4;
                    }
                    break block6;
                }
                if (f2.g[12] == 101 || f2.g[12] == 100) {
                    f3 = f2;
                    n = 101;
                } else {
                    f3 = f2;
                    n = 11;
                }
            }
            f.c(f3, n);
        }
    }

    public static void i(f f2) {
        if (f2.g[12] == 8) {
            f f3 = f.a(f2);
            if (f3 != null && f3 != g.c && f.m(f3) == 100) {
                f.d(f3, 0);
                return;
            }
            if (f3 == g.c) {
                a = null;
                f.a(0, g.c);
            }
        }
    }

    private static void G(f f2) {
        f.c(f2, false);
    }

    private static void c(f f2, boolean bl) {
        f2.g[16] = f2.g[16] | 0x200;
        if (bl) {
            f2.g[16] = f2.g[16] | 0x4000;
        }
    }

    public static void j(f f2) {
        if (!f.d(f2)) {
            f.G(f2);
            f.c(f2, 15);
        }
    }

    private static void H(f f2) {
        int n = g.h(f2.g[0], 10);
        int n2 = g.L[1];
        int n3 = 0;
        switch (n) {
            case 0: 
            case 3: 
            case 5: 
            case 7: {
                n3 = 8;
            }
        }
        int n4 = f.b(f2, n3);
        if (n4 >= 0) {
            f.a(f2, n4, -1, g.l(n2), false, 0, 0, -1, false);
        }
    }

    /*
     * Unable to fully structure code
     */
    public static boolean a(f var0, int var1_1, int var2_2) {
        block8: {
            var3_3 = g.h(var0.g[0], 10);
            var4_4 = g.l(var1_1, 5);
            var5_5 = false;
            if (var0.g[12] >= 100 || f.d(var0)) break block8;
            switch (var3_3) {
                case 1: 
                case 2: 
                case 3: 
                case 7: {
                    v0 = false;
                    break;
                }
                default: {
                    var6_6 = -1;
                    switch (g.a() % 3) {
                        case 0: {
                            v1 = var0;
                            v2 = 8;
                            ** GOTO lbl24
                        }
                        case 1: {
                            v1 = var0;
                            v3 = 4;
                            ** GOTO lbl23
                        }
                        case 2: {
                            v1 = var0;
                            v3 = 2;
lbl23:
                            // 2 sources

                            v2 = v3 & ~var0.g[25];
lbl24:
                            // 2 sources

                            var6_6 = f.b(v1, v2);
                        }
                    }
                    if (var6_6 == -1) break block8;
                    f.i(var0);
                    f.a(var0, var6_6, -1, var4_4, true, 0, var2_2, var1_1, true);
                    f.G(var0);
                    f.I(var0);
                    v0 = true;
                }
            }
            var5_5 = v0;
        }
        return var5_5;
    }

    public static boolean a(f f2, int n, boolean bl, boolean bl2) {
        int n2 = 0;
        boolean bl3 = false;
        boolean bl4 = false;
        if (f2.g[10] != 3 && f2.g[10] != 4 && f2.g[12] < 100) {
            f2.g[16] = f2.g[16] & 0xFFFFFF7F;
            int n3 = g.l(n, 4);
            int[] nArray = g.a(f2, g.c);
            int n4 = nArray[0];
            int n5 = nArray[1];
            int n6 = g.h(f2.g[0], 10);
            if (n6 == 1 && (f2.g[16] & 0x100) == 0) {
                f2.g[29] = f2.g[29] + 1;
            }
            if (!f.d(f2)) {
                f.i(f2);
            }
            boolean bl5 = false;
            boolean bl6 = false;
            for (int i = 0; i < n3; ++i) {
                int[] nArray2 = g.a(n4, n5, g.b(f2, g.c));
                int n7 = f.a(f2, nArray2[0], nArray2[1], i == 0);
                int n8 = f.b(f2, n7);
                int n9 = f.b(f2, n8, n7);
                if (f.d(f2)) {
                    n8 = -1;
                    n9 = -1;
                }
                if (n8 >= 0 && (n7 & f2.g[18]) != 0) {
                    ++n2;
                    f.a(f2, n8, n9, g.l(n), true, nArray2[0], nArray2[1], n, true);
                    switch (n6) {
                        case 0: 
                        case 3: 
                        case 5: 
                        case 7: {
                            if ((n7 & 1) == 0 || f.c(f2, n8, n9) != 0) break;
                            bl3 = true;
                        }
                    }
                    if (bl3 && !bl4) {
                        g.b(14);
                        bl4 = true;
                    }
                    if (f.c(f2, n8, n9) > 0) continue;
                    int n10 = g.d(f2.g[0], n8, 1);
                    if (n10 == -1) {
                        bl6 = true;
                    }
                    bl5 = true;
                    continue;
                }
                if (n8 >= 0 || i != n3 - 1 || n2 != 0) continue;
                g.a(g.a[4], 7, f2.a.a() + nArray2[0], f2.a.b() + nArray2[1]);
            }
            switch (n6) {
                case 0: 
                case 3: 
                case 5: 
                case 7: {
                    if (!bl6 || bl3) break;
                    g.b(24);
                }
            }
            if (n2 != 0 && (n6 != 4 && n6 != 6 || bl5)) {
                f.I(f2);
                f.f(f2, g.c.a.a, g.c.a.b, 0);
                f.c(f2);
            }
            if (bl) {
                f.c(f2, bl3 && bl2);
            }
        }
        return n2 != 0;
    }

    private static void a(f f2, int n, int n2, int n3, boolean bl, int n4, int n5, int n6, boolean bl2) {
        block22: {
            boolean bl3;
            block18: {
                int n7;
                block19: {
                    int n8;
                    int n9;
                    int n10;
                    f f3;
                    block21: {
                        block20: {
                            boolean bl4 = f.c(f2, n, -1) == -1;
                            bl3 = (f2.g[16] & 0x1000) != 0;
                            f2.g[17] = n;
                            if (!bl4) break block18;
                            if (!bl) break block19;
                            if (!bl3) break block20;
                            n7 = g.h(f2.g[0], 33);
                            boolean bl5 = false;
                            for (int i = 0; i < n7; ++i) {
                                int n11 = g.d(f2.g[0], i, 7);
                                if (f.c(f2, i, -1) == -1 || (n11 & f2.g[25]) == 0) continue;
                                f.a(f2, i, -1, n3, bl, n4, n5, n6, bl2);
                                bl5 = true;
                                break;
                            }
                            if (bl5) break block19;
                            f3 = f2;
                            n10 = n4;
                            n9 = n5;
                            n8 = 22;
                            break block21;
                        }
                        f3 = f2;
                        n10 = n4;
                        n9 = n5;
                        n8 = 4;
                    }
                    f.b(f3, n10, n9, n8);
                }
                if (g.bv < 5) {
                    ++g.bv;
                    n7 = g.d(f2.g[0], n, 8);
                    if (n7 >= 0) {
                        f.a(f2, n, n2, false, n4, n5);
                        return;
                    }
                }
                break block22;
            }
            int n12 = f.c(f2, n, n2);
            if (n12 > 0) {
                int n13;
                if (bl) {
                    n13 = 0;
                    if (n6 != -1 && (n13 = g.l(n6, 24)) == -1) {
                        n13 = 0;
                    }
                    f.b(f2, n4, n5, n13);
                }
                f.d(f2, n, n2, n3);
                int n14 = f.c(f2, n, n2);
                if (n14 <= 0) {
                    n14 = 0;
                    f.e(f2, n, n2, 0);
                    n13 = g.d(f2.g[0], n, 12);
                    int n15 = g.d(f2.g[0], n, 7);
                    int n16 = g.h(f2.g[0], 10);
                    if (n13 != -1 && (n16 != 0 && n16 != 3 && n16 != 7 || (n15 & 9) == 0)) {
                        int n17 = g.d(f2.g[0], n, 1);
                        boolean bl6 = (f2.g[16] & 0x40) != 0;
                        if (!(bl6 || n17 == -1 && bl3 || !bl2)) {
                            int n18;
                            int n19;
                            int[] nArray;
                            int n20 = 0;
                            if (n17 != -1) {
                                n20 = g.h(n17, 34);
                            }
                            if (n20 != -1 && (f2.g[16] & 0x2000) == 0) {
                                if ((f2.g[16] & 0x800) == 0) {
                                    f2.g[16] = f2.g[16] | 0x800;
                                    nArray = f2.g;
                                    n19 = 24;
                                    n18 = g.a() % 5000;
                                }
                            } else {
                                f2.g[16] = f2.g[16] & 0xFFFFF7FF;
                                f2.g[16] = f2.g[16] & 0xFFFFEFFF;
                                f2.g[16] = f2.g[16] | 0x2000;
                                nArray = f2.g;
                                n19 = 24;
                                n18 = nArray[n19] = 0;
                            }
                        }
                    }
                    if (g.N) {
                        switch (n16) {
                            case 0: 
                            case 3: 
                            case 5: 
                            case 7: {
                                if ((n15 & 1) == 0) break;
                                bl2 = false;
                            }
                        }
                    }
                    if (bl2) {
                        f.a(f2, n, n2, true, n4, n5);
                    }
                }
                g.c(n12, n14, 100, 10, -16711936);
            }
        }
    }

    private static boolean q(f f2) {
        int n;
        int n2 = g.b(f2.a.a() + f2.g[3]);
        f f3 = f.a(f2, n2, n = g.b(f2.a.b() + f2.g[4]), g.b(f2.g[5]), g.b(f2.g[6]));
        if (f3 != null) {
            f.d(f2, f3);
            return true;
        }
        return false;
    }

    private static void d(f f2, f f3) {
        f2.g[20] = 0;
        if (f3 != null) {
            int n = g.b(f3.a.a());
            int n2 = g.b(f3.a.b());
            int n3 = g.d(n, n2);
            int n4 = g.e(n, n2);
            f2.g[20] = g.a(f2.g[20], 255, n3);
            f2.g[20] = g.a(f2.g[20], 0xFFFF00, n4);
        }
    }

    private static boolean b(int n, f f2) {
        return f2 == g.c && a < 666 && !d || n != 2 && (f2.L == 0 && f2 != g.c || f2.L == 1 || f2.L == 2) && f.e(f2) != 0 && f.m(f2) < 555;
    }

    private static boolean b(f f2, f f3) {
        return f.b(g.h(f2.g[0], 10), f3);
    }

    private static f a(f f2, int n, int n2, int n3, int n4) {
        f f3 = null;
        int n5 = Integer.MAX_VALUE;
        int n6 = g.h(f2.g[0], 10);
        for (int i = 0; i < n3; ++i) {
            for (int j = 0; j < n4; ++j) {
                int n7;
                f f4 = g.a(n + i, n2 + j);
                if (f4 == null || !f.b(n6, f4) || n5 <= (n7 = g.a(f2, f4))) continue;
                n5 = n7;
                f3 = f4;
            }
        }
        return f3;
    }

    private static f c(f f2) {
        f f3 = f.a(f2);
        f2.g[15] = f2.g[15] + (int)g.d;
        if (f2.g[15] >= 500) {
            f2.g[15] = 0;
            f.q(f2);
            f3 = f.a(f2);
            if (f3 == null || f3 != g.c && f.m(f3) >= 555) {
                f.c(f2, 0);
            }
        }
        return f3;
    }

    public static void k(f f2) {
        int n;
        int n2;
        int n3;
        int n4 = 0;
        int n5 = 0;
        if (f2.g[13] == 0 && f2.g[14] == 0) {
            n3 = 1;
            n2 = 1;
            if (g.a() % 2 == 1) {
                n3 = -1;
            }
            if (g.a() % 2 == 1) {
                n2 = -1;
            }
            n4 = f2.a.a + (g.a() % 100 * n3 << 14);
            n = f2.a.b + (g.a() % 100 * n2 << 14);
        } else {
            n3 = f2.g[13] * 10000;
            n2 = f2.g[14] * 10000;
            n4 = f2.a.a + n3;
            n5 = f2.a.b + n2;
            int n6 = g.b(f2.a.a, f2.a.b, n4, n5) >> 14;
            int n7 = 1;
            if (g.a() % 2 == 1) {
                n7 = -1;
            }
            n4 = g.b(f2.a.a(), 100, -(n6 += g.a() % 45 * n7)) << 14;
            n = g.c(f2.a.b(), 100, -n6) << 14;
        }
        n5 = n;
        f.f(f2, n4, n5, 0);
    }

    private static void I(f f2) {
        int n = g.h(f2.g[0], 10);
        if (f2.g[13] == 0 && f2.g[14] == 0) {
            f.f(f2, g.c.a.a, g.c.a.b, 0);
        }
        if (n == 0) {
            int n2 = g.h(f2.g[0], 7);
            int n3 = g.h(f2.g[0], 8);
            if (f2.a.d >= n2 && f2.a.d < n2 + 4 || f2.a.d >= n3 && f2.a.d < n3 + 4) {
                int n4 = f.b(f2, false);
                if (n4 >= 100) {
                    f.c(f2, 100);
                    f.c(f2, 101);
                }
                return;
            }
        }
        f.c(f2, 14);
    }

    private static void J(f f2) {
        int n = g.h(f2.g[0], 10);
        if ((f2.g[16] & 4) == 0) {
            switch (n) {
                case 0: 
                case 3: 
                case 5: 
                case 7: {
                    g.b(11);
                }
            }
            f2.g[16] = f2.g[16] | 4;
        }
    }

    private static void K(f f2) {
        if (f2.g[13] == 0 && f2.g[14] == 0) {
            int n;
            int n2;
            int[] nArray;
            int n3;
            int[] nArray2 = g.b(f2.a);
            int n4 = f2.a.a();
            if (n4 > (n3 = nArray2[0] + (nArray2[2] - nArray2[0] >> 1))) {
                nArray = f2.g;
                n2 = 13;
                n = 16384;
            } else {
                nArray = f2.g;
                n2 = 13;
                n = -16384;
            }
            nArray[n2] = n;
            f2.g[14] = 0;
        }
    }

    /*
     * Unable to fully structure code
     */
    public static void c(f var0, int var1_1) {
        var2_2 = g.h(var0.g[0], 10);
        var3_3 = f.a(var0);
        switch (var1_1) {
            case -1: {
                g.c(var0);
                g.a(var0, 1, false);
                break;
            }
            case 0: {
                var0.g[16] = var0.g[16] & -17;
                v0 = 16;
                v1 = var0.g;
                v2 = var0.g[16] & -5;
                ** GOTO lbl140
            }
            case 1: {
                break;
            }
            case 2: {
                break;
            }
            case 4: {
                var0.g[16] = var0.g[16] & -17;
                var0.g[27] = f.g;
                if (var0.g[10] != 1 && var0.g[10] != 5) ** GOTO lbl29
                if (var0.g[10] == 5) {
                    f.K(var0);
                    var1_1 = 11;
                }
                v1 = var0.g;
                v0 = 10;
                v2 = 0;
                ** GOTO lbl140
lbl29:
                // 1 sources

                if (!f.t(var0)) break;
                if (var3_3 != null) {
                    f.f(var0, var3_3.a.a, var3_3.a.b, 0);
                }
                var1_1 = 24;
                f.J(var0);
                break;
            }
            case 5: {
                var0.g[27] = 0;
                v1 = var0.g;
                v0 = 28;
                v2 = 0;
                ** GOTO lbl140
            }
            case 14: {
                var4_4 = g.h(var0.g[0], 15) == 1;
                if (var4_4 && var0.g[12] != 14) {
                    g.c(var0);
                    var5_5 = g.l(g.L[1], 25);
                    f.d(var0, -var5_5);
                }
                f.a(var0.a.a(), var0.a.b(), 6);
                break;
            }
            case 17: {
                f.f(var0, g.c.a.a, g.c.a.b, 0);
                break;
            }
            case 15: {
                f.i(var0);
                var0.g[15] = 0;
                var0.g[16] = var0.g[16] | 16;
                v1 = var0.g;
                v0 = 17;
                v2 = 0;
                ** GOTO lbl140
            }
            case 16: {
                v1 = var0.g;
                v0 = 15;
                v2 = 0;
                ** GOTO lbl140
            }
            case 103: 
            case 104: {
                v1 = var0.g;
                v0 = 15;
                v2 = 0;
                ** GOTO lbl140
            }
            case 7: {
                switch (var2_2) {
                    case 0: {
                        var0.g[16] = var0.g[16] & -257;
                        break;
                    }
                    case 2: {
                        f.Q(var0);
                    }
                }
                break;
            }
            case 8: {
                break;
            }
            case 12: {
                v1 = var0.g;
                v0 = 27;
                v2 = f.g;
                ** GOTO lbl140
            }
            case 13: {
                break;
            }
            case 9: {
                switch (var2_2) {
                    case 2: {
                        f.P(var0);
                    }
                }
                if (var3_3 != null) {
                    f.f(var0, var3_3.a.a, var3_3.a.b, 0);
                }
                v1 = var0.g;
                v0 = 15;
                v2 = 0;
                ** GOTO lbl140
            }
            case 11: {
                break;
            }
            case 100: {
                if ((var0.g[16] & 4096) != 0) {
                    if ((var0.g[16] & 2048) == 0) {
                        var1_1 = 107;
                        break;
                    }
                    var1_1 = 4;
                    break;
                }
                g.a(var0, 1, false);
                if ((var0.g[16] & 512) == 0) break;
                g.d((var0.g[16] & 16384) != 0);
                var0.g[16] = var0.g[16] & -513;
                v0 = 16;
                v1 = var0.g;
                v2 = var0.g[16] & -16385;
                ** GOTO lbl140
            }
            case 101: {
                if ((var0.g[16] & 64) != 0) break;
                var0.g[16] = var0.g[16] | 64;
                f.g(var0);
                break;
            }
            case 106: {
                f.M(var0);
                break;
            }
            case 20: {
                if (var3_3 == null) break;
                var5_6 = g.h(var0.g[0], 12);
                f.a(var0, var3_3.a.a, var3_3.a.b, var5_6);
                break;
            }
            case 22: {
                var0.g[28] = 0;
                v1 = var0.g;
                v0 = 29;
                v2 = 0;
                ** GOTO lbl140
            }
            case 25: {
                v0 = 16;
                v1 = var0.g;
                v2 = var0.g[16] | 256;
lbl140:
                // 11 sources

                v1[v0] = v2;
            }
        }
        var0.g[12] = var1_1;
    }

    /*
     * Enabled force condition propagation
     * Lifted jumps to return sites
     */
    private static int c(f f2, int n, int n2) {
        int n3;
        int n4 = 0;
        int n5 = g.d(f2.g[0], n, 11);
        if (n5 == 0) {
            n3 = f2.g[30 + n];
            return n3;
        } else {
            if (n2 == -1) {
                int n6 = 0;
                while (n6 < n5) {
                    n4 += f.a(f2, n, n6);
                    ++n6;
                }
                return n4;
            }
            n3 = f.a(f2, n, n2);
        }
        return n3;
    }

    private static void e(f f2, int n, int n2, int n3) {
        int n4 = g.d(f2.g[0], n, 11);
        if (n4 == 0) {
            f2.g[30 + n] = n3;
            return;
        }
        if (n2 == -1) {
            for (int i = 0; i < n4; ++i) {
                f.c(f2, n, i, n3 / n4);
            }
        } else {
            f.c(f2, n, n2, n3);
        }
    }

    public static f a(f f2) {
        f f3 = null;
        int n = g.a(f2.g[20], 255);
        int n2 = g.a(f2.g[20], 0xFFFF00);
        f3 = g.b(n, n2);
        if (d && f3 == g.c) {
            return null;
        }
        if (f3 != null && f3.L != 3) {
            return f3;
        }
        return null;
    }

    private static void L(f f2) {
        int n = g.h(f2.g[0], 33);
        for (int i = 0; i < n; ++i) {
            f f3;
            int n2;
            int n3 = g.d(f2.g[0], i, 7);
            int n4 = g.d(f2.g[0], i, 12);
            if (n4 == -1) {
                n2 = g.d(f2.g[0], i, 5);
                int n5 = g.d(f2.g[0], i, 6);
                if (n2 != -1 && n5 != -1) continue;
                f3 = f2;
            } else {
                n2 = g.j(n4, 1) == 1 ? 1 : 0;
                if (n2 == 0) continue;
                f3 = f2;
            }
            f3.g[26] = f3.g[26] & ~n3;
            f2.g[25] = f2.g[25] & ~n3;
        }
        f2.g[18] = f2.g[18] & ~(f2.g[25] | f2.g[26]);
        f2.g[25] = 0;
        f2.g[26] = 0;
        f2.g[16] = f2.g[16] & 0xFFFFE7FF;
    }

    public static void l(f f2) {
        boolean bl = g.h(f2.g[0], 34) != -1;
        if (bl) {
            int n = g.h(f2.g[0], 33);
            for (int i = 0; i < n; ++i) {
                int n2 = f.c(f2, i, -1);
                if (n2 != 0) continue;
                f.M(f2);
                f2.g[25] = f2.g[25] | f2.g[26];
                f2.g[26] = 0;
                f.k(f2);
                return;
            }
        }
    }

    private static void M(f f2) {
        int n = g.h(f2.g[0], 33);
        for (int i = 0; i < n; ++i) {
            int n2;
            boolean bl;
            int n3 = f.c(f2, i, -1);
            int n4 = g.d(f2.g[0], i, 12);
            if (n4 == -1) continue;
            boolean bl2 = bl = g.j(n4, 1) == 1;
            if (n3 != 0 && !bl || ((n2 = g.d(f2.g[0], i, 7)) & f2.g[25]) != 0) continue;
            f2.g[18] = f2.g[18] | n2;
            f2.g[19] = f2.g[19] & ~n2;
            f2.g[26] = f2.g[26] | n2;
            int n5 = g.j(n4, 0);
            f.e(f2, i, -1, n5);
        }
        f2.g[16] = f2.g[16] | 0x1000;
        f2.g[16] = f2.g[16] & 0xFFFFF7FF;
        f2.g[16] = f2.g[16] & 0xFFFFFEFF;
    }

    private static int g(f f2) {
        return f.c(f2, -1);
    }

    private static int c(f f2, int n) {
        a a2 = f2.a.a;
        int n2 = f2.g[12];
        if (n != -1) {
            f2.g[12] = n;
        }
        int n3 = f.a(f2, false, true);
        int n4 = a2.a(n3);
        int n5 = a2.a(f2.a.d);
        int n6 = f2.a.e;
        f2.g[12] = n2;
        if (n4 < n5 && n6 >= n4) {
            n6 -= n4 * (n6 / n4);
        }
        return a2.b(n3, n6);
    }

    private static boolean r(f f2) {
        int n = g.h(f2.g[0], 10);
        int n2 = g.h(f2.g[0], 7);
        int n3 = f2.a.a.a(f2.a.d) >> 1;
        return (n == 0 || n == 5 || n == 3 || n == 7) && f2.a.d >= n2 && f2.a.d < n2 + 4 && f2.a.e > n3;
    }

    private static void N(f f2) {
        if ((f2.g[16] & 0x800) != 0 && f2.g[24] > 0) {
            f2.g[24] = f2.g[24] - (int)g.d;
            if (f2.g[24] <= 0) {
                f2.g[24] = 0;
                int n = g.h(f2.g[0], 34);
                if (n != -1) {
                    int n2;
                    f f3;
                    if (f2.g[12] == 101 || f2.g[12] == 100 || f.r(f2)) {
                        f3 = f2;
                        n2 = 105;
                    } else {
                        f3 = f2;
                        n2 = 106;
                    }
                    f.c(f3, n2);
                    f.c(f2);
                    return;
                }
                f2.g[16] = f2.g[16] & 0xFFFFF7FF;
            }
        }
    }

    /*
     * Enabled force condition propagation
     * Lifted jumps to return sites
     */
    private static boolean b(f f2, int n) {
        int n2 = g.h(f2.g[0], 10);
        boolean bl = false;
        boolean bl2 = g - f2.g[27] >= 500;
        switch (n2) {
            case 0: 
            case 5: 
            case 7: {
                if ((f2.g[16] & 0x1000) == 0) return bl;
                f f3 = f.a(f2);
                if (f3 == null) return bl;
                if (g.a(f2.a.a, f2.a.b, f3.a.a, f3.a.b, null, false, 197)) return bl;
                int n3 = f.b(f2);
                bl2 = bl2 && n <= 14400;
                switch (n3) {
                    case 2: 
                    case 3: {
                        bl = bl2 && g.b(f2.a.b()) == g.b(f3.a.b());
                        return bl;
                    }
                    case 0: 
                    case 1: {
                        bl = bl2 && g.b(f2.a.a()) == g.b(f3.a.a());
                    }
                }
                return bl;
            }
            case 1: {
                if ((f2.g[16] & 0x100) != 0) return bl;
                int n4 = g.h(f2.g[0], 24);
                if (n4 == -1) return bl;
                boolean bl3 = bl2;
                return bl3;
            }
            case 4: {
                f f4 = f.a(f2);
                if (f4 == null) return bl;
                if (g.a(f2.a.a, f2.a.b, f4.a.a, f4.a.b, null, false, 197)) return bl;
                return true;
            }
            case 6: {
                if (f2.g[29] < 15000) return bl;
                return true;
            }
        }
        return bl;
    }

    /*
     * Unable to fully structure code
     */
    public static void a(f var0, boolean var1_1) {
        block94: {
            block98: {
                block95: {
                    block97: {
                        block96: {
                            if (var0.g[12] == -1) break block94;
                            if (f.b == null && var0.g[10] == 2 && var0.g[12] < 100) {
                                f.b = var0;
                                f.C = f.h(var0);
                                f.D = -(f.j(var0) << 14);
                            }
                            if (f.b != null && f.D < 0 && f.b.g[12] < 100 && (f.D += (int)g.d * (var2_2 = (f.j(f.b) << 14) / 1700)) >= 0) {
                                f.D = 0;
                            }
                            f.S(var0);
                            f.C(var0);
                            f.N(var0);
                            if (var1_1) {
                                var0.a.a();
                            }
                            if (var0.g[10] != 0 && var0.g[10] != 2 && var0.g[10] != 1 && var0.g[10] != 5) break block95;
                            if (var0.g[12] == 101 || var0.g[12] == -1) break block96;
                            var2_3 = f.a(var0);
                            var3_4 = g.h(var0.g[0], 10);
                            var4_5 = g.h(var0.g[0], 12);
                            var5_6 = g.h(var0.g[0], 11);
                            var6_7 = g.h(var0.g[0], 16);
                            var7_8 = g.h(var0.g[0], 17);
                            var8_9 = g.h(var0.g[0], 18);
                            var9_10 = var6_7;
                            if (var2_3 != null) {
                                var9_10 = g.a(var0, var2_3);
                            }
                            var10_11 = g.h(var0.g[0], 15) == 1;
                            f.g = f.b(var0.g[0], var0.a.a >> 14, var0.a.b >> 14);
                            switch (var3_4) {
                                case 6: {
                                    v0 = 29;
                                    v1 = var0.g;
                                    v2 = var0.g[29] + (int)g.d;
                                    break;
                                }
                                case 0: {
                                    if ((var0.g[16] & 256) == 0) break;
                                    var4_5 += var4_5 * 120 / 100;
                                    break;
                                }
                                case 1: {
                                    var9_10 = f.a(var0, var2_3, var9_10);
                                    if (g.h(var0.g[0], 29) == -1) ** GOTO lbl50
                                    if ((var0.g[16] & 256) == 0) ** GOTO lbl47
                                    var0.g[29] = var0.g[29] + (int)g.d;
                                    if (var0.g[29] >= 5000) {
                                        var0.g[29] = 0;
                                    } else {
                                        var4_5 += var4_5 * 100 / 100;
                                        break;
lbl47:
                                        // 1 sources

                                        if (var0.g[29] < 3 || var0.g[12] != 4) break;
                                        f.c(var0, 25);
                                        break;
                                    }
lbl50:
                                    // 2 sources

                                    v0 = 16;
                                    v1 = var0.g;
                                    v2 = v1[v0] = var0.g[16] & -257;
                                }
                            }
                            if ((var0.g[16] & 128) != 0) {
                                var11_12 = g.a(var0.g[16], -65536);
                                if ((var11_12 += (int)g.d) >= 1000) {
                                    var0.g[16] = var0.g[16] & -129;
                                    var11_12 = 0;
                                }
                                v3 = var0.g;
                                v4 = 16;
                                v5 = g.a(var0.g[16], -65536, var11_12);
                            } else {
                                v4 = 16;
                                v3 = var0.g;
                                v5 = var0.g[16] & 65535;
                            }
                            v3[v4] = v5;
                            switch (var0.g[12]) {
                                case 0: {
                                    if (f.q(var0)) {
                                        f.c(var0, 4);
                                        break;
                                    }
                                    if ((var0.g[10] == 0 || var0.g[10] == 2) && g.a() % 100 < 25) {
                                        f.k(var0);
                                        f.c(var0, 1);
                                        var0.g[27] = 3000 + g.a() % 10000;
                                        break;
                                    }
                                    break block97;
                                }
                                case 1: {
                                    if (f.q(var0)) {
                                        f.c(var0, 4);
                                        break;
                                    }
                                    var0.g[15] = var0.g[15] + (int)g.d;
                                    if (var0.g[15] >= var0.g[27]) {
                                        var11_12 = var0.g[13];
                                        var12_13 = var0.g[14];
                                        f.k(var0);
                                        if (!f.d(var0, var5_6)) {
                                            var0.g[13] = var11_12;
                                            var0.g[14] = var12_13;
                                        }
                                        var0.g[15] = 0;
                                        var0.g[27] = 3000 + g.a() % 10000;
                                        break;
                                    }
                                    if (!f.d(var0, var5_6)) {
                                        if (f.c(var0, var5_6)) {
                                            var8_9 -= 10;
                                        }
                                        if (g.a() % 100 < var8_9) {
                                            f.c(var0, 2);
                                            break;
                                        }
                                        f.k(var0);
                                        break;
                                    }
                                    break block97;
                                }
                                case 2: {
                                    if (var0.a.a()) {
                                        f.c(var0, 3);
                                        break;
                                    }
                                    break block97;
                                }
                                case 3: {
                                    if (var0.a.a()) {
                                        var0.g[13] = 0;
                                        var0.g[14] = 0;
                                        f.c(var0, 0);
                                        break;
                                    }
                                    break block97;
                                }
                                case 4: {
                                    if (var2_3 == g.c) {
                                        ++f.E;
                                    }
                                    if (var9_10 >= var6_7 || !f.b(var3_4, var2_3)) {
                                        f.c(var0, 0);
                                        break;
                                    }
                                    if (var9_10 <= var7_8) {
                                        if (var3_4 == 4 || var3_4 == 6) {
                                            f.f(var0, var2_3.a.a, var2_3.a.b, 0);
                                            if (var9_10 > 2500) {
                                                if (var3_4 == 6) {
                                                    if (f.b(var0, var9_10)) {
                                                        f.c(var0, 21);
                                                        break;
                                                    }
                                                    f.c(var0, 12);
                                                    break;
                                                }
                                                if (f.b(var0, var9_10)) {
                                                    f.c(var0, 12);
                                                    break;
                                                }
                                                f.c(var0, 20);
                                                break;
                                            }
                                            f.c(var0, 7);
                                            break;
                                        }
                                        if (!g.a(var0.a.a, var0.a.b, var2_3.a.a, var2_3.a.b, null, false, 197)) {
                                            f.c(var0, 7);
                                            break;
                                        }
                                        f.c(var0, 6);
                                        break;
                                    }
                                    if (!f.b(var0, var9_10)) ** GOTO lbl149
                                    if (var3_4 == 6) {
                                        v6 = var0;
                                        v7 = 21;
                                    } else {
                                        v6 = var0;
                                        v7 = 12;
                                    }
                                    ** GOTO lbl157
lbl149:
                                    // 1 sources

                                    f.f(var0, var2_3.a.a, var2_3.a.b, 0);
                                    if (f.d(var0, var4_5)) ** GOTO lbl158
                                    if (f.a(var0, var2_3.a.a, var2_3.a.b, var4_5)) {
                                        v6 = var0;
                                        v7 = 5;
                                    } else {
                                        v6 = var0;
                                        v7 = 6;
                                    }
lbl157:
                                    // 4 sources

                                    f.c(v6, v7);
lbl158:
                                    // 2 sources

                                    f.c(var0);
                                    break;
                                }
                                case 5: {
                                    var0.g[28] = var0.g[28] + (int)g.d;
                                    var2_3 = f.c(var0);
                                    if (var2_3 == null) ** GOTO lbl185
                                    var11_12 = var0.g[13];
                                    var12_14 = var0.g[14];
                                    f.f(var0, var2_3.a.a, var2_3.a.b, 0);
                                    if (f.d(var0, var4_5) || f.a(var0, var2_3, true)) {
                                        f.c(var0, 4);
                                        break;
                                    }
                                    var0.g[13] = var11_12;
                                    var0.g[14] = var12_14;
                                    if (!f.d(var0, var4_5)) {
                                        var0.g[27] = var0.g[27] + 1;
                                        if (var0.g[27] > 3) {
                                            f.c(var0, 6);
                                            break;
                                        }
                                        f.a(var0, var2_3.a.a, var2_3.a.b, var4_5);
                                        break;
                                    }
                                    if (var0.g[28] > 5000 || var9_10 > 25600) {
                                        f.c(var0, 6);
                                        break;
                                    }
                                    break block97;
lbl185:
                                    // 1 sources

                                    f.c(var0, 0);
                                    break;
                                }
                                case 6: {
                                    var2_3 = f.c(var0);
                                    if (var2_3 != null) {
                                        f.f(var0, var2_3.a.a, var2_3.a.b, 0);
                                        if (f.c(var0, var2_3)) {
                                            f.c(var0, 4);
                                            break;
                                        }
                                        if (f.b(var0, var9_10)) {
                                            if (var3_4 == 6) {
                                                f.c(var0, 21);
                                                break;
                                            }
                                            f.c(var0, 12);
                                            break;
                                        }
                                    }
                                    break block97;
                                }
                                case 14: {
                                    if (var0.a.a() || !var10_11) {
                                        f.b(var0, true);
                                        break;
                                    }
                                    break block97;
                                }
                                case 15: {
                                    var0.g[15] = var0.g[15] + (int)g.d;
                                    if (f.a != 8 || g.a(true) != var0) {
                                        if (var0.g[15] >= 200) {
                                            if (var0.g[15] >= 400) {
                                                f.c(var0, 17);
                                                break;
                                            }
                                            f.c(var0, 16);
                                            break;
                                        }
                                        f.c(var0, 4);
                                        break;
                                    }
                                    if (var0.g[15] >= 400 && var0.a.a()) {
                                        f.H(var0);
                                        var0.a.b(var0.a.d);
                                        break;
                                    }
                                    break block97;
                                }
                                case 17: {
                                    f.d(var0, -40);
                                    if (var0.a.a()) {
                                        f.F(var0);
                                        var0.g[16] = var0.g[16] | 16;
                                        break;
                                    }
                                    break block97;
                                }
                                case 16: {
                                    var0.g[15] = var0.g[15] + (int)g.d;
                                    if (var0.g[15] >= 1000 && var0.a.a()) {
                                        var0.g[16] = var0.g[16] & -17;
                                        f.c(var0, 4);
                                        break;
                                    }
                                    break block97;
                                }
                                case 104: {
                                    var0.g[15] = var0.g[15] + (int)g.d;
                                    if (var0.a.a()) {
                                        f.F(var0);
                                    }
                                    if (var0.g[15] < 1000) {
                                        f.d(var0, -(g.cC + 100));
                                        break;
                                    }
                                    break block97;
                                }
                                case 103: {
                                    var0.g[15] = var0.g[15] + (int)g.d;
                                    if (var0.a.a()) {
                                        f.F(var0);
                                    }
                                    if (var0.g[15] < 1000) {
                                        f.d(var0, -100);
                                        break;
                                    }
                                    break block97;
                                }
                                case 9: {
                                    if (var3_4 == 2) {
                                        f.R(var0);
                                        break;
                                    }
                                    f.d(var0, -var4_5);
                                    var0.g[15] = var0.g[15] + (int)g.d;
                                    if (var0.a.a() && var0.g[15] >= 1000) {
                                        f.c(var0, 11);
                                        break;
                                    }
                                    break block97;
                                }
                                case 11: {
                                    if (var0.a.a()) {
                                        f.c(var0, 4);
                                        break;
                                    }
                                    break block97;
                                }
                                case 23: {
                                    var0.g[15] = var0.g[15] + (int)g.d;
                                    if (var0.g[15] >= 1500) {
                                        f.c(var0, 11);
                                        break;
                                    }
                                    break block97;
                                }
                                case 100: {
                                    if (var0.a.a()) {
                                        f.c(var0, 101);
                                        break;
                                    }
                                    break block97;
                                }
                                case 105: {
                                    if (var0.a.a()) {
                                        f.c(var0, 106);
                                        break;
                                    }
                                    break block97;
                                }
                                case 106: {
                                    if (var0.a.a()) {
                                        var0.g[25] = var0.g[25] | var0.g[26];
                                        var0.g[26] = 0;
                                        f.c(var0, 4);
                                        break;
                                    }
                                    break block97;
                                }
                                case 107: {
                                    if (var0.a.a()) {
                                        f.L(var0);
                                        f.c(var0, 100);
                                        break;
                                    }
                                    break block97;
                                }
                                default: {
                                    f.h(var0, var9_10);
                                    break;
                                }
                            }
                            break block97;
                        }
                        if (var0.g[12] == 101 && f.b != null && f.b == var0) {
                            f.b = null;
                        }
                    }
                    f.c(var0);
                    break block98;
                }
                if (var0.g[10] == 6) {
                    f.p(var0);
                }
            }
            f.e(var0);
        }
    }

    private static void h(f f2, int n) {
        int n2 = g.h(f2.g[0], 10);
        switch (n2) {
            case 0: 
            case 3: 
            case 5: 
            case 7: {
                f.i(f2, n);
                return;
            }
            case 1: {
                f.j(f2, n);
                return;
            }
            case 2: {
                f.R(f2);
                return;
            }
            case 4: 
            case 6: {
                f.k(f2, n);
            }
        }
    }

    public static int b(f f2) {
        int n;
        block2: {
            int n2;
            block4: {
                block6: {
                    block5: {
                        block3: {
                            n = -1;
                            if (f2.g[13] == 0 && f2.g[14] == 0) break block2;
                            if (f2.g[13] <= 8192) break block3;
                            n2 = 3;
                            break block4;
                        }
                        if (f2.g[13] >= -8192) break block5;
                        n2 = 2;
                        break block4;
                    }
                    if (f2.g[14] <= 8192) break block6;
                    n2 = 1;
                    break block4;
                }
                if (f2.g[14] >= -8192) break block2;
                n2 = 0;
            }
            n = n2;
        }
        return n;
    }

    private static boolean s(f f2) {
        int n = g.h(f2.g[0], 10);
        int n2 = g.h(f2.g[0], 7);
        int n3 = g.h(f2.g[0], 8);
        return (n == 0 || n == 5 || n == 3 || n == 7) && (f2.a.d >= n2 && f2.a.d < n2 + 4 || f2.a.d >= n3 && f2.a.d < n3 + 4);
    }

    public static boolean e(f f2) {
        int n = g.h(f2.g[0], 10);
        return f2.g[12] >= 100 || f.s(f2) || n == 2 && (f2.g[12] == 7 || f2.g[12] == 8);
    }

    public static void m(f f2) {
        if (f2.g[12] != 101 && (f2.g[10] == 0 || f2.g[10] == 2)) {
            int n = f.b(f2);
            if (n >= 0) {
                n += g.h(f2.g[0], 2);
            }
            if (n >= 0 && f2.a.d != n) {
                f2.a.b(n);
            }
        }
    }

    public static int c(f f2) {
        return f.a(f2, true, false);
    }

    private static int a(f f2, boolean bl, boolean bl2) {
        int n = 0;
        if (f2 != null && f2.a != null && f2.a.a != null) {
            int n2;
            boolean bl3;
            boolean bl4 = false;
            int n3 = g.h(f2.g[0], 10);
            n = f.b(f2);
            int n4 = 1;
            boolean bl5 = bl3 = n3 == 0 && (f2.g[16] & 0x100) != 0 || n3 == 1 && (f2.g[16] & 0x100) != 0;
            if (bl2 && (n2 = g.h(f2.g[0], 34)) == -1) {
                bl2 = false;
            }
            if (n >= 0) {
                n2 = g.h(f2.g[0], 15) == 1 ? 1 : 0;
                block0 : switch (f2.g[12]) {
                    case 0: 
                    case 6: 
                    case 28: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 0);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 2);
                        break;
                    }
                    case 1: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 1);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 3);
                        break;
                    }
                    case 5: {
                        if (f2.g[28] < 100) {
                            bl = false;
                        }
                    }
                    case 4: 
                    case 20: {
                        int n5;
                        if (bl3) {
                            n5 = n + g.h(f2.g[0], 30);
                            break;
                        }
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 2);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 4);
                        break;
                    }
                    case 7: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 3);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 5);
                        break;
                    }
                    case 8: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 4);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 6);
                        break;
                    }
                    case 12: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 7);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 23);
                        break;
                    }
                    case 13: {
                        int n5;
                        switch (n3) {
                            case 1: {
                                if (bl2) {
                                    n5 = n + (g.i(f2.g[0], 8) + f2.g[28] * 4);
                                    break block0;
                                }
                                n5 = n + (g.h(f2.g[0], 24) + f2.g[28] * 4);
                                break block0;
                            }
                        }
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 8);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 24);
                        break;
                    }
                    case 2: 
                    case 9: 
                    case 17: 
                    case 103: 
                    case 104: {
                        int n5;
                        if ((f2.g[16] & 0x1000) != 0) {
                            if (bl2) {
                                n5 = n + g.i(f2.g[0], 9);
                                break;
                            }
                            n5 = n + g.d(f2.g[0], f2.g[17], 2);
                            break;
                        }
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 5);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 7);
                        break;
                    }
                    case 23: {
                        bl4 = true;
                    }
                    case 3: 
                    case 11: 
                    case 105: {
                        int n5;
                        if ((f2.g[16] & 0x1000) != 0) {
                            if (bl2) {
                                n5 = n + g.i(f2.g[0], 9);
                                break;
                            }
                            n5 = n + g.d(f2.g[0], f2.g[17], 2);
                            break;
                        }
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 6);
                            break;
                        }
                        n5 = n + g.h(f2.g[0], 8);
                        break;
                    }
                    case 15: 
                    case 16: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 9);
                            break;
                        }
                        n5 = n + g.d(f2.g[0], f2.g[17], 2);
                        break;
                    }
                    case 14: 
                    case 18: {
                        int n5;
                        if (n2 != 0 || f2.g[12] == 18) {
                            if (bl2) {
                                n5 = n + g.i(f2.g[0], 9);
                                break;
                            }
                            n5 = n + g.d(f2.g[0], f2.g[17], 2);
                            break;
                        }
                        n5 = -1;
                        break;
                    }
                    case 100: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 10);
                            break;
                        }
                        if ((f2.g[16] & 0x18) != 0) {
                            n5 = n + g.h(f2.g[0], 27);
                            break;
                        }
                        n5 = n + g.d(f2.g[0], f2.g[17], 3);
                        break;
                    }
                    case 101: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 11);
                            break;
                        }
                        if ((f2.g[16] & 0x18) != 0) {
                            n5 = n + g.h(f2.g[0], 28);
                            break;
                        }
                        n5 = n + g.d(f2.g[0], f2.g[17], 4);
                        break;
                    }
                    case 19: {
                        n += 28;
                        break;
                    }
                    case 107: {
                        n4 = -1;
                    }
                    case 106: {
                        int n5;
                        if (bl2) {
                            n5 = n + g.i(f2.g[0], 12);
                            break;
                        }
                        if (f2.g[12] == 106 && f2.g[25] != 0) {
                            n5 = n + g.h(f2.g[0], 2);
                            break;
                        }
                        n5 = n + g.i(f2.g[0], 13);
                        break;
                    }
                    case 22: {
                        n += 43;
                        break;
                    }
                    case 21: {
                        n += 51;
                        break;
                    }
                    case 24: 
                    case 25: {
                        int n5 = n + g.h(f2.g[0], 29);
                        break;
                    }
                    case 26: {
                        int n5 = 77;
                        break;
                    }
                    case 27: 
                    case 108: {
                        int n5 = 87;
                        break;
                    }
                    default: {
                        int n5 = n = -1;
                    }
                }
            }
            if (bl4 || bl && n >= 0 && f2.a.d != n) {
                f2.a.a(n, n4, -1);
            }
        }
        return n;
    }

    private static void f(f f2, int n, int n2, int n3) {
        int n4;
        int n5;
        int n6;
        int n7;
        int[] nArray = null;
        if ((n3 & 1) != 0) {
            n7 = n;
            n6 = n2;
            n5 = f2.a.a;
            n4 = f2.a.b;
        } else {
            n7 = f2.a.a;
            n6 = f2.a.b;
            n5 = n;
            n4 = n2;
        }
        nArray = g.a(n7, n6, n5, n4, false);
        f2.g[13] = nArray[0];
        f2.g[14] = nArray[1];
    }

    public static boolean f(f f2) {
        return f2 != null && f2.g[12] < 100 && f2.g[12] != -1 && f2.g[10] != 5;
    }

    private static boolean b(int n, int n2) {
        byte by;
        block8: {
            int n3;
            byte[] byArray;
            block3: {
                int n4;
                byte[][] byArray2;
                block7: {
                    block6: {
                        block5: {
                            block4: {
                                block2: {
                                    by = 0;
                                    if (!g.b(g.b(n), g.b(n2))) break block2;
                                    byArray = g.e[g.b(n)];
                                    n3 = n2;
                                    break block3;
                                }
                                if (!g.b(g.b(n - 5), g.b(n2 + 4))) break block4;
                                byArray = g.e[g.b(n - 5)];
                                n3 = n2 + 4;
                                break block3;
                            }
                            if (!g.b(g.b(n + 4), g.b(n2 + 4))) break block5;
                            byArray = g.e[g.b(n + 4)];
                            n3 = n2 + 4;
                            break block3;
                        }
                        if (!g.b(g.b(n - 5), g.b(n2 - 5))) break block6;
                        byArray2 = g.e;
                        n4 = n - 5;
                        break block7;
                    }
                    if (!g.b(g.b(n + 4), g.b(n2 - 5))) break block8;
                    byArray2 = g.e;
                    n4 = n + 4;
                }
                byArray = byArray2[g.b(n4)];
                n3 = n2 - 5;
            }
            by = byArray[g.b(n3)];
        }
        return (by & 8) != 0;
    }

    private static boolean c(f f2, int n) {
        int n2 = f2.g[13] * (int)g.d * n / 1000;
        int n3 = f2.g[14] * (int)g.d * n / 1000;
        return f.b(f2.a.a + n2 >> 14, f2.a.b + n3 >> 14);
    }

    private static boolean c(int n, int n2) {
        return g.a(g.b(n), g.b(n2), 64) || g.a(g.b(n - 5), g.b(n2 + 4), 64) || g.a(g.b(n + 4), g.b(n2 + 4), 64) || g.a(g.b(n - 5), g.b(n2 - 5), 64) || g.a(g.b(n + 4), g.b(n2 - 5), 64);
    }

    private static boolean b(int n, int n2, int n3) {
        int n4 = g.h(n, 19);
        int n5 = g.h(n, 20);
        int n6 = n2 - (n4 * 16 >> 1) + 8;
        int n7 = n3 - (n5 * 16 >> 1) + 8;
        for (int i = 0; i < n4; ++i) {
            for (int j = 0; j < n5; ++j) {
                if (!f.c(n6 + i * 16, n7 + j * 16)) continue;
                return true;
            }
        }
        return false;
    }

    private static boolean c(int n, int n2, int n3) {
        return g.a(g.b(n), g.b(n2), n3) || g.a(g.b(n - 5), g.b(n2 + 4), n3) || g.a(g.b(n + 4), g.b(n2 + 4), n3) || g.a(g.b(n - 5), g.b(n2 - 5), n3) || g.a(g.b(n + 4), g.b(n2 - 5), n3);
    }

    private static boolean d(int n, int n2) {
        return g.e(n / 16, n2 / 16) || g.e((n - 5) / 16, (n2 + 4) / 16) || g.e((n + 4) / 16, (n2 + 4) / 16) || g.e((n - 5) / 16, (n2 - 5) / 16) || g.e((n + 4) / 16, (n2 - 5) / 16);
    }

    public static boolean a(int n, int n2, int n3) {
        return f.a(n, n2, n3, 77);
    }

    public static boolean a(int n, int n2, int n3, int n4) {
        int n5;
        int n6;
        int n7 = g.h(n, 19);
        int n8 = g.h(n, 20);
        int n9 = n2 - (n7 * 16 >> 1) + 8;
        int n10 = n3 - (n8 * 16 >> 1) + 8;
        for (n6 = 0; n6 < n7; ++n6) {
            for (n5 = 0; n5 < n8; ++n5) {
                if (!f.c(n9 + n6 * 16, n10 + n5 * 16, n4)) continue;
                return true;
            }
        }
        int n11 = g.h(n, 10);
        if (n11 == 5 || n11 == 7) {
            for (n6 = 0; n6 < n7; ++n6) {
                for (n5 = 0; n5 < n8; ++n5) {
                    if (!f.d(n9 + n6 * 16, n10 + n5 * 16)) continue;
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean c(f f2, f f3) {
        int n = f2.a.a();
        int n2 = f2.a.b();
        int n3 = f2.a.a;
        int n4 = f2.a.b;
        g.a(f2, 1, false);
        int n5 = g.h(f2.g[0], 10);
        if (n5 == 2) {
            f2.a.b(n, n2);
            if (!f.a(f2.g[0], n, n2) && f.a(f2, f3, false)) {
                g.a(f2, 0, false);
                return true;
            }
        } else {
            for (int i = -1; i <= 1; ++i) {
                for (int j = -1; j <= 1; ++j) {
                    if ((i != 0 || j == 0) && (i == 0 || j != 0)) continue;
                    int n6 = n + i * 16;
                    int n7 = n2 + j * 16;
                    f2.a.b(n6, n7);
                    if (f.a(f2.g[0], n6, n7) || !f.a(f2, f3, false)) continue;
                    g.a(f2, 0, false);
                    return true;
                }
            }
        }
        f2.a.a = n3;
        f2.a.b = n4;
        g.a(f2, 0, false);
        return false;
    }

    /*
     * Unable to fully structure code
     */
    private static boolean a(f var0, int var1_1, int var2_2, int var3_3) {
        block26: {
            block25: {
                block28: {
                    block27: {
                        block22: {
                            block24: {
                                block23: {
                                    block16: {
                                        block19: {
                                            block21: {
                                                block20: {
                                                    block13: {
                                                        block18: {
                                                            block17: {
                                                                block15: {
                                                                    block14: {
                                                                        var4_4 = false;
                                                                        g.a(var0, 1, false);
                                                                        var5_5 = 0;
                                                                        var6_6 = 0;
                                                                        if ((var0.g[16] & 128) != 0) {
                                                                            var5_5 = g.b(var0.a.a());
                                                                            var6_6 = g.b(var0.a.b());
                                                                        }
                                                                        var7_7 = var0.a.a / 16 * 16;
                                                                        var8_8 = var0.a.b / 16 * 16;
                                                                        f.f(var0, var1_1, var2_2, 0);
                                                                        var9_9 = var0.g[13];
                                                                        var10_10 = var0.g[14];
                                                                        var11_11 = var0.g[13] * (int)g.d * var3_3 / 1000;
                                                                        var12_12 = var0.g[14] * (int)g.d * var3_3 / 1000;
                                                                        var13_13 = 81920;
                                                                        if (g.d(var9_9) <= g.d(var10_10)) break block13;
                                                                        if (var10_10 == 0 || f.a(var0.g[0], var7_7 + var11_11 >> 14, var8_8 + var12_12 + (var10_10 > 0 ? var13_13 : -var13_13) >> 14) && f.a(var0.g[0], var7_7 >> 14, var8_8 + (var10_10 > 0 ? var13_13 : -var13_13) >> 14)) break block14;
                                                                        var9_9 = 0;
                                                                        v0 = var10_10 > 0 ? 1 : -1;
                                                                        v1 = 14;
                                                                        ** GOTO lbl74
                                                                    }
                                                                    if (var9_9 == 0 || f.a(var0.g[0], var7_7 + var11_11 + (var9_9 > 0 ? var13_13 : -var13_13) >> 14, var8_8 + var12_12 >> 14) && f.a(var0.g[0], var7_7 + (var9_9 > 0 ? var13_13 : -var13_13) >> 14, var8_8 >> 14)) break block15;
                                                                    var9_9 = (var9_9 > 0 ? 1 : -1) << 14;
                                                                    v2 = 0;
                                                                    break block16;
                                                                }
                                                                if (var10_10 <= 0) break block17;
                                                                var9_9 = 0;
                                                                v2 = 16384;
                                                                break block16;
                                                            }
                                                            if (var10_10 >= 0) break block18;
                                                            var9_9 = 0;
                                                            v2 = -16384;
                                                            break block16;
                                                        }
                                                        var9_9 = 0;
                                                        v0 = g.a() % 100 < 50 ? 1 : -1;
                                                        v1 = 14;
                                                        ** GOTO lbl74
                                                    }
                                                    if (g.d(var9_9) >= g.d(var10_10)) break block19;
                                                    if (var9_9 == 0 || f.a(var0.g[0], var7_7 + var11_11 + (var9_9 > 0 ? var13_13 : -var13_13) >> 14, var8_8 + var12_12 >> 14) && f.a(var0.g[0], var7_7 + (var9_9 > 0 ? var13_13 : -var13_13) >> 14, var8_8 >> 14)) break block20;
                                                    var9_9 = (var9_9 > 0 ? 1 : -1) << 14;
                                                    v2 = 0;
                                                    break block16;
                                                }
                                                if (var10_10 == 0 || f.a(var0.g[0], var7_7 + var11_11 >> 14, var8_8 + var12_12 + (var10_10 > 0 ? var13_13 : -var13_13) >> 14) && f.a(var0.g[0], var7_7 >> 14, var8_8 + (var10_10 > 0 ? var13_13 : -var13_13) >> 14)) break block21;
                                                var9_9 = 0;
                                                v0 = var10_10 > 0 ? 1 : -1;
                                                v1 = 14;
                                                ** GOTO lbl74
                                            }
                                            if (var9_9 > 0) {
                                                var9_9 = 16384;
                                                v2 = 0;
                                            } else if (var9_9 < 0) {
                                                var9_9 = -16384;
                                                v2 = 0;
                                            } else {
                                                var9_9 = (g.a() % 100 < 50 ? 1 : -1) << 14;
                                                v2 = 0;
                                            }
                                            break block16;
                                        }
                                        if (g.d(var1_1 - var7_7) < g.d(var2_2 - var8_8)) {
                                            var9_9 = (var9_9 >= 0 ? 1 : -1) << 14;
                                            v2 = 0;
                                        } else {
                                            var9_9 = 0;
                                            v0 = var10_10 >= 0 ? 1 : -1;
                                            v1 = 14;
lbl74:
                                            // 4 sources

                                            v2 = v0 << v1;
                                        }
                                    }
                                    var10_10 = v2;
                                    var11_11 = var9_9 * (int)g.d * var3_3 / 1000;
                                    var12_12 = var10_10 * (int)g.d * var3_3 / 1000;
                                    if (var11_11 == 0 || f.a(var0.g[0], var7_7 + var11_11 >> 14, var8_8 >> 14)) break block22;
                                    var0.g[13] = var9_9;
                                    var0.g[14] = 0;
                                    if ((var0.g[16] & 128) == 0) break block23;
                                    var14_14 = g.b(var7_7 + var11_11 >> 14);
                                    var15_15 = g.b(var8_8 + var12_12 >> 14);
                                    if (var14_14 != var5_5 || var15_15 != var6_6) break block24;
                                }
                                var0.a.a = var7_7 + var11_11;
                                var0.a.b = var8_8;
                            }
                            v3 = true;
                            break block25;
                        }
                        if (var12_12 == 0 || f.a(var0.g[0], var7_7 >> 14, var8_8 + var12_12 >> 14)) break block26;
                        var0.g[13] = 0;
                        var0.g[14] = var10_10;
                        if ((var0.g[16] & 128) == 0) break block27;
                        var14_14 = g.b(var7_7 + var11_11 >> 14);
                        var15_15 = g.b(var8_8 + var12_12 >> 14);
                        if (var14_14 != var5_5 || var15_15 != var6_6) break block28;
                    }
                    var0.a.a = var7_7;
                    var0.a.b = var8_8 + var12_12;
                }
                v3 = true;
            }
            var4_4 = v3;
        }
        g.a(var0, 0, false);
        return var4_4;
    }

    private static boolean d(f f2, int n) {
        boolean bl;
        block12: {
            int n2;
            int n3;
            block9: {
                block11: {
                    block10: {
                        bl = false;
                        g.a(f2, 1, false);
                        int n4 = 0;
                        int n5 = 0;
                        if ((f2.g[16] & 0x80) != 0) {
                            n4 = g.b(f2.a.a());
                            n5 = g.b(f2.a.b());
                        }
                        n3 = f2.a.a;
                        n2 = f2.a.b;
                        int n6 = f2.g[13] * (int)g.d * n / 1000;
                        int n7 = f2.g[14] * (int)g.d * n / 1000;
                        if (f.a(f2.g[0], (n3 += n6) >> 14, (n2 += n7) >> 14) && !g) break block9;
                        if ((f2.g[16] & 0x80) == 0) break block10;
                        int n8 = g.b(n3 >> 14);
                        int n9 = g.b(n2 >> 14);
                        if (n8 != n4 || n9 != n5) break block11;
                    }
                    f2.a.a = n3;
                    f2.a.b = n2;
                }
                bl = true;
                break block12;
            }
            if (f.a(f2.g[0], f2.a.a(), f2.a.b())) {
                n3 = f2.a.a() / 16 * 16 + 8;
                if (!f.a(f2.g[0], n3, n2 = f2.a.b() / 16 * 16 + 8)) {
                    f2.a.b(n3, n2);
                    bl = true;
                } else {
                    int n10 = n3 - 16;
                    int n11 = n3 + 16;
                    int n12 = n2 - 16;
                    int n13 = n2 + 16;
                    block0: for (int i = n10; i < n11; i += 16) {
                        for (int j = n12; j < n13; j += 16) {
                            if (f.a(f2.g[0], i, j)) continue;
                            f2.a.b(i, j);
                            bl = true;
                            continue block0;
                        }
                    }
                }
            }
        }
        g.a(f2, 0, false);
        return bl;
    }

    public static int a(f f2, int n) {
        int n2;
        block5: {
            int n3;
            block6: {
                block4: {
                    n2 = 8;
                    int n4 = g.h(f2.g[0], 10);
                    if (n == 1) {
                        n2 = 136;
                    }
                    if (n4 != 2) break block4;
                    n2 = 128;
                    if (n != 0 || f2.g[12] != 7 && f2.g[12] != 8) break block5;
                    n3 = 0;
                    break block6;
                }
                if (!f.s(f2) || n != 0) break block5;
                n3 = 128;
            }
            n2 = n3;
        }
        return n2;
    }

    public static boolean g(f f2) {
        return f2.g[10] != 5 && f2.g[10] != 3 && f2.g[10] != 4 && f2.g[12] < 100 && f2.g[12] > -1;
    }

    /*
     * Unable to fully structure code
     */
    public static void n(f var0) {
        block12: {
            block8: {
                block10: {
                    block7: {
                        block11: {
                            block9: {
                                block5: {
                                    block6: {
                                        var1_1 = g.h(var0.g[0], 10);
                                        if (var0.g[12] != 101) break block5;
                                        if (var1_1 != 1) break block6;
                                        v0 = var0;
                                        v1 = var0.a.b() - 8;
                                        break block7;
                                    }
                                    v0 = var0;
                                    v2 = (var0.a.b() << 8) + var0.a.a() >> 1;
                                    break block8;
                                }
                                if ((var1_1 == 5 || var1_1 == 7) && var0.g[12] != -1 && (var0.g[16] & 32) != 0) {
                                    f.f = true;
                                }
                                if (var0.g[10] != 4) break block9;
                                v0 = var0;
                                v3 = (var0.a.b() + 320 << 8) + var0.a.a();
                                v4 = 240;
                                break block10;
                            }
                            if (var1_1 != 0 && var1_1 != 3 && var1_1 != 5 && var1_1 != 7 || var0.g[12] != 8) break block11;
                            var2_2 = f.a(var0);
                            if (var2_2 == null) break block12;
                            switch (f.b(var0)) {
                                case 1: 
                                case 2: {
                                    v5 = var0;
                                    v6 = var2_2.a.b() - 1;
                                    ** GOTO lbl31
                                }
                                case 0: 
                                case 3: {
                                    v5 = var0;
                                    v6 = var2_2.a.b() + 1;
lbl31:
                                    // 2 sources

                                    v5.M = (v6 << 8) + var2_2.a.a();
                                }
                            }
                            return;
                        }
                        v0 = var0;
                        v1 = var0.a.b();
                    }
                    v3 = v1 << 8;
                    v4 = var0.a.a();
                }
                v2 = v3 + v4;
            }
            v0.M = v2;
        }
    }

    private static void a(int n, int n2, int n3) {
        int n4 = g.b(n) - n3;
        int n5 = g.b(n2) - n3;
        n3 <<= 1;
        for (int i = 0; i < n3; ++i) {
            for (int j = 0; j < n3; ++j) {
                f f2 = g.a(n4 + i, n5 + j);
                if (f2 == null || f2.L != 3 || f2.g[12] >= 4 || f2.g[12] == -1 || f2.g[10] == 3 || f2.g[10] == 6 || f2.g[10] == 4 || f2.g[10] == 5) continue;
                f.d(f2, g.c);
                f.c(f2, 4);
            }
        }
    }

    private static boolean a(f f2, f f3, boolean bl) {
        boolean bl2 = true;
        if (f3 != null && f.b(f2, f3)) {
            int n = g.h(f2.g[0], 10);
            if (bl) {
                g.a(f2, 1, false);
            }
            g.a(f3, 1, true);
            int n2 = 0;
            int n3 = 0;
            if (n == 4 || n == 6) {
                n2 = 2;
                n3 = 128;
            }
            bl2 = g.a(f2.a.a, f2.a.b, f3.a.a, f3.a.b, null, false, 197, n2, n3);
            int n4 = 16 * g.h(f2.g[0], 19) / 2 - 5 << 14;
            int n5 = 16 * g.h(f2.g[0], 20) / 2 - 5 << 14;
            if (!bl2) {
                bl2 = g.a(f2.a.a - n4, f2.a.b - n5, f3.a.a - n4, f3.a.b - n5, null, false, 197, n2, n3);
            }
            if (!bl2) {
                bl2 = g.a(f2.a.a + n4, f2.a.b - n5, f3.a.a + n4, f3.a.b - n5, null, false, 197, n2, n3);
            }
            if (!bl2) {
                bl2 = g.a(f2.a.a + n4, f2.a.b + n5, f3.a.a + n4, f3.a.b + n5, null, false, 197, n2, n3);
            }
            if (!bl2) {
                bl2 = g.a(f2.a.a - n4, f2.a.b + n5, f3.a.a - n4, f3.a.b + n5, null, false, 197, n2, n3);
            }
            if (bl) {
                g.a(f2, 0, false);
            }
            g.a(f3, 0, true);
        }
        return !bl2;
    }

    /*
     * Unable to fully structure code
     */
    private static boolean t(f var0) {
        block6: {
            var1_1 = false;
            var2_2 = g.h(var0.g[0], 10);
            var3_3 = g.h(var0.g[0], 29);
            if (var3_3 == -1 || var2_2 != 0 || g.h(var0.g[0], 34) != -1 || (var0.g[16] & 4356) != 0) break block6;
            var4_4 = 20;
            switch (g.bF) {
                case 0: {
                    v0 = 20;
                    ** GOTO lbl18
                }
                case 1: {
                    v0 = 35;
                    ** GOTO lbl18
                }
                case 2: {
                    v0 = 50;
                    ** GOTO lbl18
                }
                case 3: {
                    v0 = 65;
lbl18:
                    // 4 sources

                    var4_4 = v0;
                }
            }
            var1_1 = g.a() % 100 < var4_4;
        }
        return var1_1;
    }

    private static void i(f f2, int n) {
        int n2 = g.h(f2.g[0], 12);
        int n3 = g.h(f2.g[0], 17);
        f f3 = f.a(f2);
        switch (f2.g[12]) {
            case 7: {
                f.d(f2, n2);
                if (!f2.a.a()) break;
                if (f3 != null && n <= n3 && !g.a(f2.a.a, f2.a.b, f3.a.a, f3.a.b, null, false, 197) && (f3 == g.c && a != 100 && a != 14 && a != 17 && (a != 18 || g.m(f3.g[29], 1) != 1) || f3 != g.c && f.m(f3) < 555)) {
                    f.f(f2, f3.a.a, f3.a.b, 0);
                    f2.g[15] = 0;
                    f.c(f2, 8);
                    if (f3 == g.c) {
                        f.b(f3, g.h(f2.g[0], 14));
                        g.cu = g.h(f.a(g.c, f2, true));
                        a = f2;
                        g.b();
                        g.j();
                        f.a(100, g.c);
                        return;
                    }
                    f.g(f3, f2.a.a, f2.a.b, 0);
                    f.d(f3, 100);
                    if (f.e(f3) != 3) break;
                    f.c(f3);
                    return;
                }
                if (f3 != null) {
                    f.c(f2, 4);
                    return;
                }
                f.c(f2, 0);
                return;
            }
            case 8: {
                if (f3 != null && !g.a(f2.a.a, f2.a.b, f3.a.a, f3.a.b, null, false, 197)) {
                    f2.g[15] = f2.g[15] + (int)g.d;
                    if (f2.g[15] < 1000) break;
                    g.b(21);
                    f2.g[15] = 0;
                    int n4 = g.h(f2.g[0], 14);
                    if (f3 == null) break;
                    if (f3 == g.c) {
                        if (a == 100) {
                            f.b(g.c, n4);
                            return;
                        }
                        f.c(f2, 4);
                        return;
                    }
                    if (f.e(f3) == 0) break;
                    f.o(f3, n4);
                    if (f.m(f3) < 555) {
                        f.c(f2, 9);
                        f.d(f3, 101);
                        return;
                    }
                    f.c(f2, 0);
                    return;
                }
                f.i(f2);
                f.c(f2, 4);
                return;
            }
            case 12: {
                if (!f2.a.a()) break;
                f.c(f2, 13);
                if (f3 == null || (!f.b(f2, n) || f3 != g.c || a == 100 || a == 14 || a == 17) && (f3 == g.c || f.m(f3) >= 555)) break;
                int n5 = g.h(f2.g[0], 14) << 1;
                if (f3 == g.c) {
                    f.a(f2.g[13], f2.g[14]);
                    f.b(f3, n5);
                    return;
                }
                f.o(f3, n5);
                return;
            }
            case 13: {
                if (!f2.a.a()) break;
                f.c(f2, 4);
                return;
            }
            case 24: {
                if (!f2.a.a()) break;
                f2.g[16] = f2.g[16] | 0x100;
                f.c(f2, 4);
                return;
            }
            case 26: 
            case 27: 
            case 28: 
            case 108: {
                f.p(f2);
            }
        }
    }

    public static void o(f f2) {
        block2: {
            block6: {
                int n;
                f f3;
                block4: {
                    block5: {
                        block3: {
                            int n2 = g.h(f2.g[0], 10);
                            if (n2 != 0) break block2;
                            f.i(f2);
                            if (f2.g[12] != 0) break block3;
                            f2.g[13] = 0;
                            f2.g[14] = -16384;
                            f3 = f2;
                            n = 26;
                            break block4;
                        }
                        if (f2.g[12] != 14) break block5;
                        f3 = f2;
                        n = 100;
                        break block4;
                    }
                    if (f2.g[12] >= 100) break block6;
                    f3 = f2;
                    n = 28;
                }
                f.c(f3, n);
            }
            f.c(f2);
            g.a(f2, 0, false);
            return;
        }
        f2.g[10] = 0;
    }

    public static void p(f f2) {
        block17: {
            int n;
            f f3;
            block19: {
                int n2;
                block18: {
                    n2 = g.h(f2.g[0], 10);
                    if (n2 != 0) break block17;
                    if (f2.g[10] != 0) break block18;
                    if (f2.g[12] != 108) break block17;
                    f3 = f2;
                    n = 100;
                    break block19;
                }
                if (f2.g[10] != 6) break block17;
                switch (f2.g[12]) {
                    case 26: {
                        i = true;
                        if (f2.a.a()) {
                            f.c(f2, 27);
                            f.c(f2);
                            h = true;
                            return;
                        }
                        break block17;
                    }
                    case 27: {
                        return;
                    }
                    case 28: {
                        if (h || !i && f2.a.a()) {
                            f.c(f2, 27);
                            f.c(f2);
                            return;
                        }
                        break block17;
                    }
                    case 108: {
                        int n3 = f2.a.a.a(f2.a.d);
                        if (f2.a.e >= n3 / 4) {
                            f.c(f2, 100);
                            f2.g[10] = 0;
                            f.c(f2);
                            return;
                        }
                        break block17;
                    }
                    case 14: {
                        f.c(f2);
                        if (f2.a.a()) {
                            int n4 = f.b(f2, false);
                            n2 = g.h(f2.g[0], 10);
                            if (n2 == 0 && n4 != 100 && n4 != 101) {
                                f.c(f2, 27);
                                f.c(f2);
                                return;
                            }
                            if (n2 == 0) {
                                f.c(f2, 108);
                                f.c(f2);
                                return;
                            }
                            f.c(f2, n4);
                            f2.g[10] = 0;
                            f.c(f2);
                            return;
                        }
                        break block17;
                    }
                    case -1: 
                    case 100: 
                    case 101: {
                        f2.g[10] = 0;
                        return;
                    }
                    default: {
                        f3 = f2;
                        n = 26;
                    }
                }
            }
            f.c(f3, n);
        }
    }

    private static boolean u(f f2) {
        return f2.g[12] == 8 && f.a(f2) != null;
    }

    /*
     * Unable to fully structure code
     */
    public static int[] b(f var0, boolean var1_1, boolean var2_2) {
        block7: {
            var3_3 = g.s;
            var4_4 = f.a(var0);
            if (var4_4 == null) break block7;
            var6_5 = var4_4.a.a - (g.T >> 14 << 14);
            var7_6 = var4_4.a.b - ((g.U >> 14) - 0 << 14);
            var8_7 = 262144;
            var9_8 = 0;
            if (f.s != 0 && var2_2) {
                var9_8 = g.a() % 3 - 1 << 14;
            }
            switch (f.b(var0)) {
                case 0: {
                    var3_3[0] = var6_5;
                    v0 = var3_3;
                    v1 = 1;
                    v2 = var7_6 + (var8_7 >> 1) + var9_8;
                    ** GOTO lbl36
                }
                case 1: {
                    var3_3[0] = var6_5;
                    v0 = var3_3;
                    v1 = 1;
                    v2 = var7_6 - var8_7 + var9_8;
                    ** GOTO lbl36
                }
                case 2: {
                    v3 = var3_3;
                    v4 = 0;
                    v5 = var6_5 + var8_7;
                    ** GOTO lbl32
                }
                case 3: {
                    v3 = var3_3;
                    v4 = 0;
                    v5 = var6_5 - var8_7;
lbl32:
                    // 2 sources

                    v3[v4] = v5 + var9_8;
                    v0 = var3_3;
                    v1 = 1;
                    v2 = var7_6;
lbl36:
                    // 3 sources

                    v0[v1] = v2;
                }
            }
        }
        return var3_3;
    }

    private static void d(f f2, boolean bl) {
        if (f.u(f2)) {
            int[] nArray = f.b(f2, bl, true);
            f2.a.a = nArray[0];
            f2.a.b = nArray[1];
        }
    }

    private static int a(f f2, f f3, int n) {
        int n2;
        if (f3 != null && f2 != null && (n2 = g.h(f2.g[0], 10)) == 1) {
            int n3 = g.h(f2.g[0], 33);
            if (n3 == 3) {
                n = g.a(f2.a.a(), f2.a.b() + 10, f3.a.a(), f3.a.b());
            }
            for (int i = 0; i < n3; ++i) {
                int n4;
                int n5 = g.d(f2.g[0], i, 9);
                if (n5 == 0 || (n4 = g.a(f2.a.a() + n5, f2.a.b(), f3.a.a(), f3.a.b())) >= n) continue;
                n = n4;
            }
        }
        return n;
    }

    /*
     * Unable to fully structure code
     */
    private static void j(f var0, int var1_1) {
        var2_2 = g.h(var0.g[0], 12);
        var4_3 = g.h(var0.g[0], 17);
        var5_4 = f.a(var0);
        block0 : switch (var0.g[12]) {
            case 12: {
                if (f.g - var0.g[27] <= 1500 || var1_1 > 14400) ** GOTO lbl11
                var0.g[28] = 0;
                v0 = var0;
                v1 = 13;
                ** GOTO lbl48
lbl11:
                // 1 sources

                if (f.g - var0.g[27] >= 0 && var1_1 <= 14400) break;
                f.c(var0, 13);
                var0.g[28] = 1;
                return;
            }
            case 13: {
                switch (var0.g[28]) {
                    case 0: {
                        if (!var0.a.a() || var5_4 == null) break;
                        g.a(var0.a.a, g.h(var0.g[0], 25), var0.a.a, var0.a.b, var5_4.a.a, var5_4.a.b, 50, 200);
                        var0.g[28] = var0.g[28] + 1;
                        break block0;
                    }
                    case 1: {
                        if (!var0.a.a()) break;
                        f.c(var0, 4);
                    }
                }
                return;
            }
            case 7: {
                f.d(var0, var2_2);
                if (!var0.a.a()) break;
                if (var1_1 > var4_3 || f.a == 100) ** GOTO lbl38
                f.f(var0, var5_4.a.a, var5_4.a.b, 0);
                var0.g[15] = 0;
                if (var5_4 == g.c) {
                    f.b(g.c, g.h(var0.g[0], 14));
                }
                v0 = var0;
                v1 = 8;
                ** GOTO lbl48
lbl38:
                // 1 sources

                v0 = var0;
                ** GOTO lbl47
            }
            case 8: {
                if (!var0.a.a()) break;
                ** GOTO lbl46
            }
            case 25: {
                if (!var0.a.a()) break;
                var0.g[29] = 0;
lbl46:
                // 2 sources

                v0 = var0;
lbl47:
                // 2 sources

                v1 = 4;
lbl48:
                // 3 sources

                f.c(v0, v1);
            }
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void O(f var0) {
        switch (var0.g[12]) {
            case 7: {
                v0 = var0.a;
                v1 = v0;
                v2 = v0.b;
                v3 = g.k[var0.g[28]].g;
                v4 = 10;
                ** GOTO lbl22
            }
            case 8: {
                var1_1 = g.c.a.a.a(0, var0.g[27]);
                var0.a.a += var1_1[0] + (var1_1[2] >> 1) << 14;
                v5 = var0.a;
                v1 = v5;
                v6 = v5.b + (var1_1[1] + (var1_1[3] >> 1) << 14);
                ** GOTO lbl23
            }
            case 9: {
                v7 = var0.a;
                v1 = v7;
                v2 = v7.b;
                v3 = var0.g;
                v4 = 28;
lbl22:
                // 2 sources

                v6 = v2 - v3[v4];
lbl23:
                // 2 sources

                v1.b = v6;
            }
        }
    }

    private static void P(f f2) {
        int n = 0;
        do {
            f2.a.a = g.c.a.a + (g.a() % 131072 - 65536);
            f2.a.b = g.c.a.b + (g.a() % 131072 - 65536);
        } while (f.a(f2.g[0], f2.a.a(), f2.a.b()) && ++n < 10);
        int n2 = g.a(g.c.a.a, 0);
        if (f2.g[27] >= 0 && f2.g[27] < n2) {
            byte[] byArray = g.c.a.a.a(0, f2.g[27]);
            f2.g[28] = g.d(byArray[1] + (byArray[3] >> 1) << 14);
        }
    }

    private static void Q(f f2) {
        f f3;
        int n = g.a(g.c.a.a, 0);
        if (t < n) {
            f2.g[27] = t++;
            f2.g[28] = g.a(f2.a.a, f2.a.b, g.c.a.a, g.c.a.b, 50, 200);
            if (f2.g[28] >= 0) {
                f2.g[15] = 0;
                return;
            }
            f3 = f2;
        } else {
            f3 = f2;
        }
        f.c(f3, 4);
    }

    private static void R(f f2) {
        int n = g.h(f2.g[0], 12);
        switch (f2.g[12]) {
            case 9: {
                f2.g[15] = f2.g[15] + (int)g.d;
                if (f2.g[28] > 0) {
                    f2.g[28] = f2.g[28] - 0x320000 * (int)g.d / 1000;
                    f.d(f2, -(n << 1));
                    return;
                }
                f.c(f2, 10);
                return;
            }
            case 10: {
                f2.g[15] = f2.g[15] + (int)g.d;
                if (f2.g[15] < 3000) break;
                f.c(f2, 11);
                return;
            }
            case 7: {
                g.a(f2, 1, false);
                f2.g[15] = f2.g[15] + (int)g.d;
                f2.a.a = g.k[f2.g[28]].a.a;
                f2.a.b = g.k[f2.g[28]].a.b;
                if (g.a(g.c.a, f2.a)) {
                    if (a == 3 || a == 2 || f.e()) {
                        f.G(f2);
                        f.a(f2, 0, -1, true, 0, 0);
                        f.c(f2, 100);
                        if (--t >= 0) break;
                        t = 0;
                        return;
                    }
                    f.b(g.c, g.h(f2.g[0], 14));
                    f.c(f2, 8);
                    f.a(0, g.c);
                    return;
                }
                if (!g.c(f2.g[28])) break;
                if (--t < 0) {
                    t = 0;
                }
                f.c(f2, 4);
                return;
            }
            case 8: {
                b = true;
                g.b();
                f2.a.a = g.c.a.a;
                f2.a.b = g.c.a.b + 2;
            }
        }
    }

    private static void S(f f2) {
        int[] nArray;
        int n = g.h(f2.g[0], 10);
        if (n == 2 && f2.g[12] != 8 && f2.g[12] != 9 && f2.g[12] != 100 && f2.g[12] != 101 && (nArray = g.b(f2.a)) != null && g.a(nArray[0], nArray[1], nArray[2], nArray[3], g.c.a.a(), g.c.a.b()) && (f.d() || f.e())) {
            f.G(f2);
            f.a(f2, 0, -1, true, 0, 0);
            f.c(f2, 100);
        }
    }

    public static void b(f f2, f f3) {
        int n = g.h(f2.g[0], 10);
        if ((n == 4 || n == 6) && f2.g[12] != 7 && f2.g[12] != 8 && f2.g[12] != 13 && f2.g[12] != 19 && f2.g[12] != 18) {
            f.f(f2, f3.a.a, f3.a.b, 0);
            f.c(f2, 18);
            f.c(f2);
        }
    }

    private static boolean v(f f2) {
        int n = g.h(f2.g[0], 10);
        return n == 6 && f2.g[12] == 18;
    }

    /*
     * Unable to fully structure code
     */
    private static void k(f var0, int var1_1) {
        var2_2 = g.h(var0.g[0], 10);
        var4_3 = f.a(var0);
        switch (var0.g[12]) {
            case 18: {
                if (!var0.a.a()) break;
                v0 = var0;
                v1 = 1;
                ** GOTO lbl102
            }
            case 12: {
                if (!var0.a.a()) break;
                if (var4_3 != null) {
                    f.f(var0, var4_3.a.a, var4_3.a.b, 0);
                    var0.g[15] = 0;
                    f.c(var0, 13);
                    var0.g[16] = var0.g[16] & -257;
                    return;
                }
                v0 = var0;
                v1 = 0;
                ** GOTO lbl102
            }
            case 13: {
                if ((var0.g[16] & 256) == 0) {
                    f.T(var0);
                }
                if (!var0.a.a()) break;
                if (var2_2 != 6) ** GOTO lbl33
                if (g.a() % 100 >= 40) ** GOTO lbl30
                if (f.a(var0, var4_3, true)) ** GOTO lbl100
                v0 = var0;
                v1 = 20;
                ** GOTO lbl102
lbl30:
                // 1 sources

                v0 = var0;
                v1 = 19;
                ** GOTO lbl102
lbl33:
                // 1 sources

                v0 = var0;
                v1 = 19;
                ** GOTO lbl102
            }
            case 19: {
                if (!var0.a.a() || var4_3 == null) break;
                f.f(var0, var4_3.a.a, var4_3.a.b, 0);
                if (f.a(var0, var4_3, true)) ** GOTO lbl100
                v0 = var0;
                v1 = 20;
                ** GOTO lbl102
            }
            case 20: {
                if (var4_3 == null) break;
                var5_4 = g.h(var0.g[0], 12);
                if (!f.d(var0, var5_4)) ** GOTO lbl100
                if (!f.a(var0, var4_3, true)) break;
                f.f(var0, var4_3.a.a, var4_3.a.b, 0);
                v0 = var0;
                v1 = 12;
                ** GOTO lbl102
            }
            case 7: {
                var5_5 = g.h(var0.g[0], 12);
                f.d(var0, var5_5);
                if (var1_1 > 2500) ** GOTO lbl78
                f.f(var0, var4_3.a.a, var4_3.a.b, 0);
                var0.g[15] = 0;
                if (var4_3 == g.c) {
                    if (f.a != 16) {
                        f.b(g.c, g.h(var0.g[0], 14));
                        if (f.a == 11 || f.a == 10) {
                            g.e(false);
                        }
                        f.a(var0.g[13], var0.g[14]);
                        f.b(var4_3, var0, true);
                        v0 = var0;
                        v1 = 8;
                    } else {
                        v0 = var0;
                        v1 = 19;
                    }
                } else {
                    f.e(var4_3, g.h(var0.g[0], 14));
                    f.g(var4_3, var0.a.a, var0.a.b, 1);
                    f.d(var4_3, 102);
                    v0 = var0;
                    v1 = 8;
                }
                ** GOTO lbl102
lbl78:
                // 1 sources

                v0 = var0;
                ** GOTO lbl101
            }
            case 8: {
                if (!var0.a.a()) break;
                ** GOTO lbl100
            }
            case 21: {
                if (!var0.a.a()) break;
                v0 = var0;
                v1 = 22;
                ** GOTO lbl102
            }
            case 22: {
                if (var4_3 != null && var0.g[28] < 6 && g.bv < 5) {
                    var0.g[28] = var0.g[28] + 1;
                    var5_6 = g.a() % 60 - 30;
                    var6_7 = g.a() % 60 - 30;
                    var5_6 = var0.a.a > var4_3.a.a ? (var5_6 -= 60) : (var5_6 += 60);
                    var6_7 = var0.a.b > var4_3.a.b ? (var6_7 -= 60) : (var6_7 += 60);
                    var7_8 = f.a(var0, true, false);
                    g.b(var0.a.a, 47, var0.a.a, var0.a.b, var4_3.a.a + (var5_6 << 14), var4_3.a.b + (var6_7 << 14), var7_8[0], var7_8[1], 100, 200, var0.g[0] + 1, var0.g[2], var0.g[1]);
                }
                if (!var0.a.a()) break;
                var0.g[28] = 0;
                var0.g[29] = 0;
lbl100:
                // 5 sources

                v0 = var0;
lbl101:
                // 2 sources

                v1 = 4;
lbl102:
                // 12 sources

                f.c(v0, v1);
            }
        }
    }

    private static void T(f f2) {
        g.a(f2, 1, true);
        int[] nArray = g.s;
        int n = (int)g.d;
        int n2 = f2.a.a;
        int n3 = f2.a.b;
        int n4 = n2;
        int n5 = n3;
        int n6 = f2.g[13] * n * 150 / 1000;
        int n7 = f2.g[14] * n * 150 / 1000;
        f2.a.a += n6;
        f2.a.b += n7;
        f f3 = null;
        boolean bl = false;
        boolean bl2 = false;
        do {
            f f4;
            int n8;
            bl = g.a(n2, n3, n2 + n6, n3 + n7, nArray, false, 13, 2, 136);
            if (f3 != null) {
                if (f3.L < 9) {
                    g.a(f3, 0, true);
                } else {
                    g.a(f3, false);
                }
                f3 = null;
            }
            if (!bl) continue;
            int n9 = g.b(nArray[0] >> 14);
            if (g.b(n9, n8 = g.b(nArray[1] >> 14), 140)) {
                n2 = nArray[0];
                n3 = nArray[1];
                f3 = g.a(n9, n8);
                if (f3 != null) {
                    if (f3.L < 9) {
                        switch (f3.L) {
                            case 3: {
                                int n10 = g.h(f3.g[0], 10);
                                if (n10 != 0 && n10 != 3 && n10 != 7 && n10 != 2) break;
                                f.l(f3, n10);
                                break;
                            }
                            case 1: {
                                break;
                            }
                            case 0: {
                                if (f3 != g.c || a == 16) break;
                                f.b(f3, g.h(f2.g[0], 14));
                                if (a == 11 || a == 10) {
                                    g.e(false);
                                }
                                f.a(f2.g[13], f2.g[14]);
                                f.b(f3, f2, false);
                            }
                        }
                        g.a(f3, 1, true);
                        continue;
                    }
                    switch (f3.L) {
                        case 9: {
                            if (f.a(f3, 0)) break;
                        }
                        default: {
                            g.d(f3);
                            break;
                        }
                    }
                    continue;
                }
                f4 = f2;
            } else {
                f4 = f2;
            }
            f4.a.a = nArray[0] - 16 * f2.g[13];
            f2.a.b = nArray[1] - 16 * f2.g[14];
            f2.g[16] = f2.g[16] | 0x100;
            bl = false;
            bl2 = true;
        } while (bl);
        if (bl2 && f.a(f2.g[0], f2.a.a >> 14, f2.a.b >> 14)) {
            f2.g[16] = f2.g[16] | 0x100;
            f2.a.a = n4;
            f2.a.b = n5;
        }
        g.a(f2, 0, true);
    }

    private static void l(f f2, int n) {
        f.i(f2);
        int n2 = 0;
        if (n == 2) {
            // empty if block
        }
        n2 = f.b(f2, 1);
        f.a(f2, n2, -1, 100, true, 0, 0, -1, true);
        f.I(f2);
    }

    private static boolean w(f f2) {
        boolean bl = false;
        int n = g.h(f2.g[0], 33);
        for (int i = 0; i < n && !bl; ++i) {
            int n2 = g.d(f2.g[0], i, 11);
            if (n2 <= 0) continue;
            bl = true;
        }
        return bl;
    }

    private static int h(f f2) {
        int n = 0;
        int n2 = g.h(f2.g[0], 33);
        for (int i = 0; i < n2; ++i) {
            int n3 = g.d(f2.g[0], i, 11);
            if (n3 <= 0) continue;
            for (int j = 0; j < n3; ++j) {
                n += g.d(f2.g[0], i, j, 0);
            }
        }
        return n;
    }

    private static int i(f f2) {
        int n = 0;
        int n2 = g.h(f2.g[0], 33);
        for (int i = 0; i < n2; ++i) {
            int n3 = g.d(f2.g[0], i, 11);
            if (n3 <= 0) continue;
            for (int j = 0; j < n3; ++j) {
                n += f.c(f2, i, j);
            }
        }
        return n;
    }

    private static int j(f f2) {
        int n = 0;
        int n2 = g.h(f2.g[0], 33);
        for (int i = 0; i < n2; ++i) {
            int n3;
            int n4 = g.d(f2.g[0], i, 1);
            if (n4 != -1) continue;
            int n5 = g.d(f2.g[0], i, 11);
            if (n5 == 0) {
                if ((f2.g[16] & 0x1000) == 0) {
                    n += g.d(f2.g[0], i, 0);
                    continue;
                }
                n3 = g.d(f2.g[0], i, 12);
                n += g.j(n3, 0);
                continue;
            }
            for (n3 = 0; n3 < n5; ++n3) {
                if ((f2.g[16] & 0x1000) == 0) {
                    n += g.d(f2.g[0], i, n3, 0);
                    continue;
                }
                System.out.println("#WARNING: CObject_Enemy.ENEMY_GetTotalHealth: Mutated enemies with subparts not supported yet.");
            }
        }
        return n;
    }

    private static int k(f f2) {
        int n = 0;
        if (f2.g[12] != 100 && f2.g[12] != 101) {
            int n2 = g.h(f2.g[0], 33);
            for (int i = 0; i < n2; ++i) {
                int n3 = g.d(f2.g[0], i, 1);
                if (n3 != -1) continue;
                int n4 = f.c(f2, i, -1);
                n += n4;
            }
        }
        return n;
    }

    public static void b(Graphics graphics, f f2) {
        boolean bl = f.w(b);
        byte[] byArray = g.a[12].a(8, 2);
        g.a[12].a(graphics, 8, 0, 0, 0);
        g.a(graphics, g.a[12], 0, 0, 0, 1, 0, f.j(f2), f.k(f2) + (D >> 14), byArray[0] & 0xFF, byArray[1] & 0xFF, byArray[2] & 0xFF, byArray[3] & 0xFF, 0, 0, 64);
        if (bl) {
            byArray = g.a[12].a(8, 3);
            g.a(graphics, g.a[12], 14, 0, 14, 1, 0, C, f.i(f2) + (D >> 14), byArray[0] & 0xFF, byArray[1] & 0xFF, byArray[2] & 0xFF, byArray[3] & 0xFF, 0, 0, 64);
        }
        byArray = g.a[12].a(8, 0);
        g.a(graphics, g.b, null, 9, g.h(f2.g[0], 31), 0, byArray[0] & 0xFF, byArray[1] & 0xFF, byArray[2] & 0xFF, byArray[3] & 0xFF, 0, 6);
        if (bl) {
            byArray = g.a[12].a(8, 1);
            g.a(graphics, g.b, null, 9, g.h(f2.g[0], 31) + 1, 0, byArray[0] & 0xFF, byArray[1] & 0xFF, byArray[2] & 0xFF, byArray[3] & 0xFF, 0, 6);
        }
    }

    public static void d(int[] nArray) {
        nArray[22] = -1;
        nArray[25] = 0;
        nArray[26] = 0;
        nArray[27] = 0;
        nArray[28] = 0;
        nArray[29] = 0;
        nArray[30] = 0;
        nArray[31] = 0;
        nArray[32] = 0;
        nArray[33] = 0;
        nArray[34] = 0;
        nArray[35] = 0;
        nArray[36] = 0;
        nArray[39] = 0;
    }

    public static int[] a(int[] nArray, int n, int n2) {
        int[] nArray2 = new int[nArray.length + 4 + 15];
        int[] nArray3 = nArray2;
        nArray2[26] = n;
        nArray3[27] = n2;
        nArray3[28] = -2;
        nArray3[29] = -2;
        System.arraycopy((Object)nArray, (int)0, (Object)nArray3, (int)0, (int)nArray.length);
        nArray3[30] = 0;
        nArray3[31] = 0;
        nArray3[32] = 0;
        nArray3[33] = 0;
        nArray3[34] = 0;
        nArray3[35] = 0;
        nArray3[36] = 0;
        nArray3[37] = 0;
        nArray3[38] = 0;
        nArray3[39] = 0;
        nArray3[40] = 0;
        nArray3[41] = 0;
        nArray3[43] = g.a(nArray3[43], 65280, -1);
        nArray3[44] = 0;
        return nArray3;
    }

    private static int l(f f2) {
        int n = 0;
        n = f2.L == 1 ? f2.g[16] : 5;
        return n;
    }

    public static int d(f f2) {
        int n = 24;
        if (f2.L != 1) {
            n = 29;
        }
        return n;
    }

    public static int e(f f2) {
        int n = 0;
        if (f2.L == 1) {
            // empty if block
        }
        n = f2.g[17];
        return n;
    }

    private static void m(f f2, int n) {
        if (f2.L == 1) {
            // empty if block
        }
        f2.g[17] = n;
    }

    private static boolean x(f f2) {
        boolean bl = false;
        int n = (int)g.d;
        int n2 = f.d(f2);
        int n3 = n2 + 2;
        f2.g[n3] = f2.g[n3] - n;
        if (f2.g[n2 + 2] <= 0) {
            bl = true;
            f2.g[n2 + 2] = 1000 + g.a() % 500;
            int n4 = f.e(f2);
            if (f2.L == 0 && (n4 == 2 || n4 == 4 || n4 == 5)) {
                int n5 = n2 + 2;
                f2.g[n5] = f2.g[n5] >> 1;
            }
        }
        return bl;
    }

    public static f b(f f2) {
        int n = f.d(f2);
        if (f2.g[n + 15] != 0) {
            int n2 = g.a(f2.g[n + 15], 255);
            int n3 = g.a(f2.g[n + 15], 0xFFFF00);
            f f3 = g.b(n2, n3);
            return f3;
        }
        return g.c;
    }

    public static void c(f f2, f f3) {
        int n = f.d(f2);
        f2.g[n + 15] = 0;
        if (f3 != null) {
            int n2 = g.b(f3.a.a());
            int n3 = g.b(f3.a.b());
            int n4 = g.d(n2, n3);
            int n5 = g.e(n2, n3);
            f2.g[n + 15] = g.a(f2.g[n + 15], 255, n4);
            f2.g[n + 15] = g.a(f2.g[n + 15], 0xFFFF00, n5);
            if (f2.g[n + 15] == 0) {
                System.out.println("WARNING: NPC_SetFollowTargetObject: Cannot get target from collision map");
            }
            f.d(f2, 0);
            f.m(f2, 2);
        }
    }

    public static void a(f f2, f f3, boolean bl) {
        f.g(f2, f3.a.a, f3.a.b, 0);
        f.d(f2, 0);
        if (f2.L == 1) {
            int n = 0 + f.a(f2, bl);
            f2.a.b(n);
            return;
        }
        f.ad(f2);
    }

    public static void d(f f2, int n) {
        int n2 = f.d(f2);
        if (f2.g[n2 + 1] != n) {
            int n3 = n2 + 14;
            f2.g[n3] = f2.g[n3] & 0xFFFFFFFE;
        }
        f2.g[n2 + 1] = n;
        switch (f2.g[n2 + 1]) {
            case 7: {
                f.Z(f2);
                return;
            }
            case 8: {
                f.Y(f2);
            }
        }
    }

    private static void n(f f2, int n) {
        int n2 = f.d(f2);
        int n3 = n2 + 14;
        f2.g[n3] = f2.g[n3] | n;
    }

    private static int m(f f2) {
        int n = f.d(f2);
        return f2.g[n + 1];
    }

    /*
     * Unable to fully structure code
     */
    private static void U(f var0) {
        block19: {
            var1_1 = f.d(var0);
            if (var0.g[var1_1 + 1] < 100 && f.x(var0)) {
                f.W(var0);
                f.X(var0);
                var2_2 = 0;
                var2_2 = f.y(var0) != false ? f.o(var0) : f.n(var0);
                f.d(var0, var2_2);
            }
            if (var0.g[var1_1 + 1] < 4) break block19;
            var2_3 = null;
            var3_4 = g.a(var0, f.b(var0));
            switch (var0.g[var1_1 + 1]) {
                case 4: {
                    if (var3_4 <= 2560) break;
                    v0 = var0;
                    v1 = 5;
                    ** GOTO lbl93
                }
                case 5: {
                    if (var3_4 <= 2048) {
                        v0 = var0;
                        v1 = 4;
                    } else {
                        if (var3_4 < 6656) break;
                        v0 = var0;
                        v1 = 6;
                    }
                    ** GOTO lbl93
                }
                case 6: {
                    if (var3_4 >= 6144) break;
                    v0 = var0;
                    v1 = 5;
                    ** GOTO lbl93
                }
                case 101: {
                    if (!var0.a.a()) break;
                    v0 = var0;
                    v1 = 0;
                    ** GOTO lbl93
                }
                case 8: {
                    if (f.z(var0)) break;
                    v0 = var0;
                    v1 = 7;
                    ** GOTO lbl93
                }
                case 7: {
                    if (!f.z(var0)) break;
                    v0 = var0;
                    v1 = 8;
                    ** GOTO lbl93
                }
                case 102: {
                    if (!var0.a.a()) break;
                    if (!f.j(var0)) ** GOTO lbl52
                    v0 = var0;
                    v1 = 104;
                    ** GOTO lbl93
lbl52:
                    // 1 sources

                    v0 = var0;
                    ** GOTO lbl92
                }
                case 104: {
                    if (!var0.a.a()) break;
                    v0 = var0;
                    v1 = 0;
                    ** GOTO lbl93
                }
                case 555: {
                    if (!var0.a.a()) break;
                    f.d(var0, 556);
                    var5_5 = g.a(var0.a.a(), var0.a.b() + 1, true, f.a(var0, false), false);
                    var0.g[var1_1 + 14] = g.a(var0.g[var1_1 + 14], 0xFF0000, var5_5);
                    return;
                }
                case 103: {
                    if (!var0.a.a()) break;
                    v2 = var1_1 + 13;
                    var0.g[v2] = var0.g[v2] + 1;
                    if (g.l(var0.g[28], 2) == 1 && var0.g[var1_1 + 13] < g.l(var0.g[28], 13)) {
                        v3 = var0.g;
                        v4 = var1_1 + 2;
                        v5 = 0;
                    } else {
                        var0.g[var1_1 + 13] = 0;
                        v3 = var0.g;
                        v4 = var1_1 + 2;
                        v5 = 5000;
                    }
                    v3[v4] = v5;
                    v0 = var0;
                    v1 = 9;
                    ** GOTO lbl93
                }
                case 556: {
                    var4_6 = g.a(var0.g[var1_1 + 14], 0xFF0000);
                    if (!g.g[var4_6].a.a()) break;
                    f.j = true;
                    g.a(var0.a.a(), var0.a.b() + 1, false, f.a(var0, false), false);
                    return;
                }
                case 666: {
                    if (!var0.a.a()) break;
                    v0 = var0;
lbl92:
                    // 2 sources

                    v1 = 667;
lbl93:
                    // 11 sources

                    f.d(v0, v1);
                }
            }
        }
    }

    private static int n(f f2) {
        int n = f.d(f2);
        int n2 = f.l(f2);
        int n3 = 0;
        if ((f2.g[n + 14] & 2) == 0 || f.e(f2) == 1) {
            switch (n2) {
                case 5: {
                    int n4 = 80;
                    break;
                }
                case 4: {
                    int n4 = 60;
                    break;
                }
                case 3: {
                    int n4 = 40;
                    break;
                }
                case 2: {
                    int n4 = n3 = 20;
                }
            }
            if (g.a() % 100 < n3) {
                f.b(f2, g.a() % 8, true);
                return 1;
            }
            return 0;
        }
        return 4;
    }

    private static void V(f f2) {
        if (f2 != null && f2.L == 0) {
            int n = f2.g[28];
            if (f.n(f2)) {
                int n2 = g.g(f2.g[4]);
                f2.g[28] = -2;
                for (int i = 0; i < g.c[n2].length; ++i) {
                    int n3;
                    if (g.c[n2][i] == -1 || (n3 = g.n(g.c[n2][i])) == -1 || n3 == n || f.a(g.l(n3, 18))) continue;
                    f2.g[28] = n3;
                    return;
                }
            }
        }
    }

    private static int o(f f2) {
        int n = f.d(f2);
        int n2 = f.e(f2);
        if ((f2.g[n + 14] & 2) == 0 || n2 == 1) {
            int[] nArray = f.c(f2);
            int n3 = nArray[0];
            boolean bl = false;
            f.b(f2, n3, true);
            return 3;
        }
        if (f2.L == 0 && (n2 == 4 || n2 == 5)) {
            f.V(f2);
            int n4 = f2.g[28];
            if (n4 >= 0 && (a != null || c != null)) {
                int n5 = g.a(f2, f.b(f2));
                f f3 = c;
                int n6 = J;
                if (a != null) {
                    f3 = a;
                    n6 = g.a(f2, a);
                }
                f.g(f2, f3.a.a, f3.a.b, 0);
                int n7 = g.l(n4, 11);
                if (n2 == 4 && n5 > 2560) {
                    return 6;
                }
                if (n6 > n7) {
                    if (n2 == 4) {
                        if (a == null) {
                            return 9;
                        }
                        return 6;
                    }
                    f.g(f2, f3.a.a, f3.a.b, 0);
                    return 3;
                }
                g.a(f3, f2, n4);
                return 103;
            }
        }
        return 8;
    }

    private static boolean y(f f2) {
        int n = f.d(f2);
        for (int i = 0; i < 8; ++i) {
            if (f2.g[n + 3 + i] <= 0) continue;
            return true;
        }
        return false;
    }

    private static void W(f f2) {
        int n = f.d(f2);
        for (int i = 0; i < 8; ++i) {
            int n2;
            int n3;
            int[] nArray;
            if (f2.g[n + 3 + i] <= 1) {
                nArray = f2.g;
                n3 = n + 3 + i;
                n2 = 0;
            } else {
                nArray = f2.g;
                n3 = n + 3 + i;
                n2 = f2.g[n + 3 + i] >> 1;
            }
            nArray[n3] = n2;
        }
    }

    private static void X(f f2) {
        J = -1;
        c = null;
        int n = f.d(f2);
        f f3 = f.b(f2);
        if (f2.L == 1) {
            int n2 = n + 14;
            f2.g[n2] = f2.g[n2] & 0xFFFFFFFD;
        }
        int n3 = (f2.a.a >> 14) / 16;
        int n4 = (f2.a.b >> 14) / 16;
        for (int i = n3 - 20; i <= n3 + 20; ++i) {
            for (int j = n4 - 20; j <= n4 + 20; ++j) {
                int n5;
                f f4;
                if (i < 0 || j < 0 || (f4 = g.a(i, j)) == null) continue;
                int n6 = f2.a.a;
                int n7 = f2.a.b;
                int n8 = f4.a.a;
                int n9 = f4.a.b;
                int n10 = 0;
                switch (f4.L) {
                    case 3: {
                        if (f4.g[10] == 3 || f4.g[10] == 6 || f4.g[10] == 4 || f4.g[10] == 5 || f4.g[12] >= 100) break;
                        n10 = 10;
                        if (f2.L != 0) break;
                        n5 = g.a(f2, f4);
                        if (J != -1 && J <= n5 || g.a(n6, n7, n8, n9, null, false, 1)) break;
                        J = n5;
                        c = f4;
                        break;
                    }
                    case 0: 
                    case 1: {
                        if (f4 != f3) break;
                        int n11 = n + 14;
                        f2.g[n11] = f2.g[n11] | 2;
                    }
                }
                if (n10 == 0) continue;
                n5 = g.b(n6, n7, n8, n9);
                for (int k = 0; k < 8; ++k) {
                    if (!g.c(k, n5)) continue;
                    int n12 = n + 3 + k;
                    f2.g[n12] = f2.g[n12] + n10;
                    if (n10 <= 0) continue;
                    f.c(f2, k, n10);
                }
            }
        }
        f.aa(f2);
    }

    private static boolean z(f f2) {
        int[] nArray = f.b(f2);
        return g.b(nArray[0], nArray[1], 13) ? g.a(nArray[0] - 2, nArray[1] - 2, nArray[0] + 2, nArray[1] + 2, g.b(f2.a.a()), g.b(f2.a.b())) : nArray[0] == g.b(f2.a.a()) && nArray[1] == g.b(f2.a.b());
    }

    private static void Y(f f2) {
        f f3 = f.b(f2);
        int n = 0;
        int n2 = 0x5A0000;
        int n3 = (f3.a.a >> 14) / 16;
        int n4 = (f3.a.b >> 14) / 16;
        boolean bl = false;
        for (int i = n3 - 20; i <= n3 + 20; ++i) {
            for (int j = n4 - 20; j <= n4 + 20; ++j) {
                f f4 = g.a(i, j);
                if (f4 == null || f4.L != 3) continue;
                bl = true;
                int n5 = g.b(f3.a.a, f3.a.b, f4.a.a, f4.a.b);
                if (n5 > n) {
                    n = n5;
                }
                if (n5 >= n2) continue;
                n2 = n5;
            }
        }
        if (bl) {
            H = -(n + n2 >> 1 >> 14);
            if (n - n2 >> 14 < 225) {
                H += 180;
                return;
            }
        } else {
            I = 0;
            H = 0;
            f.e[0] = g.b(f3.a.a());
            f.e[1] = g.b(f3.a.b());
        }
    }

    private static void Z(f f2) {
        int[] nArray = f.b(f2);
        int n = g.c(nArray[0]) + 8 << 14;
        int n2 = g.c(nArray[1]) + 8 << 14;
        f.g(f2, n, n2, 0);
    }

    private static int[] b(f f2) {
        int[] nArray = e;
        f f3 = f.b(f2);
        if (H != I) {
            I = H;
            int n = H;
            int n2 = 786432;
            int n3 = g.b(f3.a.a, n2, n);
            int n4 = g.c(f3.a.b, n2, n);
            nArray[0] = g.b(n3 >> 14);
            nArray[1] = g.b(n4 >> 14);
        }
        return nArray;
    }

    private static void aa(f f2) {
        g.a(f2, 1, true);
        int n = f.d(f2);
        int n2 = f2.a.a;
        int n3 = f2.a.b;
        int n4 = n + 11;
        int n5 = n + 12;
        int n6 = f2.g[n4];
        int n7 = f2.g[n5];
        int n8 = 16;
        if (f2.L == 0) {
            n8 = 32;
        }
        for (int i = 0; i < 8; ++i) {
            f.b(f2, i, false);
            n4 = n + 11;
            n5 = n + 12;
            int n9 = n2 + 320 * f2.g[n4];
            int n10 = n3 + 320 * f2.g[n5];
            int[] nArray = g.s;
            if ((f2.g[n + 14] & 4) != 0) {
                g.a(n2, n3, n9, n10, nArray, false, 13, n8, 0);
            } else {
                g.a(n2, n3, n9, n10, nArray, false, 13);
            }
            int n11 = g.a(n2 >> 14, n3 >> 14, nArray[0] >> 14, nArray[1] >> 14);
            int n12 = 102400;
            int n13 = 10 * n11 / n12;
            int n14 = n + 3 + i;
            f2.g[n14] = f2.g[n14] - n13;
        }
        g.a(f2, 0, true);
        f2.g[n4] = n6;
        f2.g[n5] = n7;
    }

    private static void c(f f2, int n, int n2) {
        int n3 = f.d(f2);
        int n4 = n3 + 3 + n - 1;
        if (n == 0) {
            n4 = n3 + 10;
        }
        int n5 = n4;
        f2.g[n5] = f2.g[n5] + (n2 >> 1);
        n4 = n3 + 3 + n + 1;
        if (n == 7) {
            n4 = n3 + 3;
        }
        int n6 = n4;
        f2.g[n6] = f2.g[n6] + (n2 >> 1);
    }

    private static int[] c(f f2) {
        int n = 0;
        int n2 = 1000000;
        int[] nArray = g.s;
        int n3 = f.d(f2);
        for (int i = 0; i < 8; ++i) {
            int n4 = f2.g[n3 + 3 + i];
            if (n4 >= n2) continue;
            nArray[0] = n = i;
            nArray[1] = n2 = n4;
        }
        return nArray;
    }

    private static boolean A(f f2) {
        return f2.L == 1 && f.b(f2) == g.c && (f2.g[17] == 2 || f2.g[17] == 4);
    }

    private static boolean B(f f2) {
        int n = f.d(f2);
        for (int i = 0; i < 8; ++i) {
            int n2 = f2.g[n + 3 + i];
            if (n2 <= 0) continue;
            return true;
        }
        return false;
    }

    private static void b(f f2, int n, boolean bl) {
        int n2;
        int n3;
        block9: {
            int n4;
            block8: {
                block7: {
                    int n5;
                    n3 = f2.a.a;
                    n2 = f2.a.b;
                    if (n == 7 || n == 0 || n == 1) {
                        n5 = n3 + 819200;
                    } else if (n == 5 || n == 4 || n == 3) {
                        n5 = n3 = n3 - 819200;
                    }
                    if (n != 3 && n != 2 && n != 1) break block7;
                    n4 = n2 - 819200;
                    break block8;
                }
                if (n != 5 && n != 6 && n != 7) break block9;
                n4 = n2 + 819200;
            }
            n2 = n4;
        }
        int[] nArray = g.a(f2.a.a, f2.a.b, n3, n2, false);
        int n6 = f.d(f2);
        f2.g[n6 + 11] = nArray[0];
        f2.g[n6 + 12] = nArray[1];
        if (bl) {
            f2.g[n6 + 14] = g.a(f2.g[n6 + 14], -268435456, n);
        }
    }

    private static void ab(f f2) {
        int n;
        int n2 = f.d(f2);
        int n3 = 16;
        if (f2.L == 0) {
            n3 = 32;
        }
        if ((f2.g[n2 + 14] & 4) == 0 && ((n = g.f(g.b(f2.a.a()), g.b(f2.a.b()))) & n3) != 0) {
            int n4 = n2 + 14;
            f2.g[n4] = f2.g[n4] | 4;
        }
    }

    public static boolean h(f f2) {
        int n = f.d(f2);
        return (f2.g[n + 14] & 0x10) != 0;
    }

    public static void a(f f2, boolean bl, int n, int n2, boolean bl2) {
        int n3 = f.e(f2);
        int n4 = f.d(f2);
        int n5 = n4 + 14;
        f2.g[n5] = f2.g[n5] & 0xFFFFFFEF;
        boolean bl3 = f.m(f2) < 555;
        boolean bl4 = false;
        if (f != null && bl3 && n == f[12] && n2 == f[13] && f.b(f2) == g.c) {
            f[10] = f[10] + 1;
            bl4 = true;
        }
        if ((bl2 || bl4) && f2.L == 1 && (n3 == 2 || n3 == 4) && bl3) {
            ++F;
            if (!bl2 && bl4 || !bl || (f2.g[n4 + 14] & 2) == 0) {
                ++G;
                int n6 = n4 + 14;
                f2.g[n6] = f2.g[n6] | 0x10;
            }
        }
    }

    public static void q(f f2) {
        int n = f.d(f2);
        int n2 = n + 14;
        f2.g[n2] = f2.g[n2] & 0xFFFFFFDF;
        f2.a.a();
        int n3 = f.e(f2);
        if (n3 != 3 && n3 != 0) {
            if (f.m(f2) < 667) {
                f.ab(f2);
                f.U(f2);
                f.ac(f2);
            } else {
                g.a(f2, 1, true);
            }
            f.ad(f2);
        } else {
            g.a(f2, 0, true);
        }
        if (j) {
            j = false;
            f.h(f2);
        }
    }

    private static void g(f f2, int n, int n2, int n3) {
        int n4;
        int n5;
        int n6;
        int n7;
        int n8 = f.d(f2);
        int[] nArray = null;
        if ((n3 & 1) != 0) {
            n7 = n;
            n6 = n2;
            n5 = f2.a.a;
            n4 = f2.a.b;
        } else {
            n7 = f2.a.a;
            n6 = f2.a.b;
            n5 = n;
            n4 = n2;
        }
        nArray = g.a(n7, n6, n5, n4, false);
        f2.g[n8 + 11] = nArray[0];
        f2.g[n8 + 12] = nArray[1];
    }

    private static void ac(f f2) {
        int n = f.d(f2);
        int n2 = f2.g[n + 1];
        int n3 = f2.g[n + 11];
        int n4 = f2.g[n + 12];
        boolean bl = n2 == 5 || n2 == 6;
        boolean bl2 = n2 == 7;
        int n5 = 60;
        f f3 = f.b(f2);
        switch (n2) {
            case 3: 
            case 6: 
            case 7: {
                n5 = 80;
            }
            case 1: 
            case 5: {
                if ((f2.g[n + 14] & 1) == 0) {
                    if (bl) {
                        f.g(f2, f3.a.a, f3.a.b, 0);
                    }
                    if (f.e(f2, n5)) break;
                    if (f.a(f2, n5, true)) {
                        int n6 = n + 14;
                        f2.g[n6] = f2.g[n6] | 1;
                        return;
                    }
                    f.d(f2, 0);
                    return;
                }
                if (bl) {
                    f.g(f2, f3.a.a, f3.a.b, 0);
                } else if (bl2) {
                    f.Z(f2);
                } else {
                    int n7 = g.a(f2.g[n + 14], -268435456);
                    f.b(f2, n7, true);
                }
                boolean bl3 = f.e(f2, n5);
                if (!bl3 || f.b(f2, bl, n5)) {
                    f2.g[n + 11] = n3;
                    f2.g[n + 12] = n4;
                    if (f.a(f2, n5, false)) break;
                    int n8 = n + 14;
                    f2.g[n8] = f2.g[n8] & 0xFFFFFFFE;
                    f.d(f2, 0);
                    return;
                }
                int n9 = n + 14;
                f2.g[n9] = f2.g[n9] & 0xFFFFFFFE;
                return;
            }
            case 102: {
                f.e(f2, 100);
            }
        }
    }

    private static boolean e(f f2, int n) {
        boolean bl = false;
        int n2 = f.d(f2);
        boolean bl2 = (f2.g[n2 + 14] & 4) != 0;
        boolean bl3 = (f2.g[n2 + 14] & 8) != 0;
        g.a(f2, 1, true);
        int n3 = f2.a.a;
        int n4 = f2.a.b;
        int n5 = f2.g[n2 + 11] * (int)g.d * n / 1000;
        int n6 = f2.g[n2 + 12] * (int)g.d * n / 1000;
        if (!f.a((n3 += n5) >> 14, (n4 += n6) >> 14, bl2, bl3, f2.L == 0)) {
            f2.a.a = n3;
            f2.a.b = n4;
            bl = true;
        }
        g.a(f2, 0, true);
        return bl;
    }

    private static boolean b(f f2, boolean bl, int n) {
        int n2;
        int n3 = f.d(f2);
        f f3 = f.b(f2);
        int n4 = 0;
        int n5 = 0;
        if (bl) {
            n4 = f3.a.a;
            n2 = f3.a.b;
        } else {
            n4 = f2.a.a + f2.g[n3 + 11] * (int)g.d * n / 1000;
            n2 = f2.a.b + f2.g[n3 + 12] * (int)g.d * n / 1000;
        }
        n5 = n2;
        g.a(f3, 1, true);
        g.a(f2, 1, false);
        boolean bl2 = g.a(f2.a.a, f2.a.b, n4, n5, null, false, 13);
        g.a(f3, 0, true);
        g.a(f2, 0, false);
        return bl2;
    }

    /*
     * Unable to fully structure code
     */
    private static boolean a(f var0, int var1_1, boolean var2_2) {
        block26: {
            block25: {
                block24: {
                    block17: {
                        block20: {
                            block18: {
                                block23: {
                                    block22: {
                                        block21: {
                                            block19: {
                                                g.a(var0, 1, true);
                                                var3_3 = false;
                                                var4_4 = f.d(var0);
                                                var5_5 = (var0.g[var4_4 + 14] & 4) != 0;
                                                var6_6 = (var0.g[var4_4 + 14] & 8) != 0;
                                                var7_7 = var0.a.a / 16 * 16;
                                                var8_8 = var0.a.b / 16 * 16;
                                                var9_9 = 0;
                                                var10_10 = 0;
                                                var11_11 = var0.g[var4_4 + 11];
                                                var12_12 = var0.g[var4_4 + 12];
                                                if (!var2_2) break block17;
                                                var13_13 = 81920;
                                                var9_9 = var11_11 * (int)g.d * var1_1 / 1000;
                                                var10_10 = var12_12 * (int)g.d * var1_1 / 1000;
                                                if (g.d(var11_11) <= g.d(var12_12)) break block18;
                                                if (f.a(var7_7 + var9_9 >> 14, var8_8 + var10_10 + var13_13 >> 14, var5_5, var6_6, var0.L == 0)) break block19;
                                                var11_11 = 0;
                                                v0 = 16384;
                                                break block20;
                                            }
                                            if (f.a(var7_7 + var9_9 >> 14, var8_8 + var10_10 - var13_13 >> 14, var5_5, var6_6, var0.L == 0)) break block21;
                                            var11_11 = 0;
                                            v0 = -16384;
                                            break block20;
                                        }
                                        if (var12_12 <= 0) break block22;
                                        var11_11 = 0;
                                        v0 = 16384;
                                        break block20;
                                    }
                                    if (var12_12 >= 0) break block23;
                                    var11_11 = 0;
                                    v0 = -16384;
                                    break block20;
                                }
                                var11_11 = 0;
                                v1 = g.a() % 100 < 50 ? 1 : -1;
                                v2 = 14;
                                ** GOTO lbl69
                            }
                            if (g.d(var11_11) < g.d(var12_12)) {
                                if (!f.a(var7_7 + var9_9 + var13_13 >> 14, var8_8 + var10_10 >> 14, var5_5, var6_6, var0.L == 0)) {
                                    var11_11 = 16384;
                                    v0 = 0;
                                } else if (!f.a(var7_7 + var9_9 - var13_13 >> 14, var8_8 + var10_10 >> 14, var5_5, var6_6, var0.L == 0)) {
                                    var11_11 = -16384;
                                    v0 = 0;
                                } else if (var11_11 > 0) {
                                    var11_11 = 16384;
                                    v0 = 0;
                                } else if (var11_11 < 0) {
                                    var11_11 = -16384;
                                    v0 = 0;
                                } else {
                                    var11_11 = (g.a() % 100 < 50 ? 1 : -1) << 14;
                                    v0 = 0;
                                }
                            } else if (g.a() % 100 < 50) {
                                var11_11 = (g.a() % 100 < 50 ? 1 : -1) << 14;
                                v0 = 0;
                            } else {
                                var11_11 = 0;
                                v1 = g.a() % 100 < 50 ? 1 : -1;
                                v2 = 14;
lbl69:
                                // 2 sources

                                v0 = v1 << v2;
                            }
                        }
                        var12_12 = v0;
                    }
                    var9_9 = var11_11 * (int)g.d * var1_1 / 1000;
                    var10_10 = var12_12 * (int)g.d * var1_1 / 1000;
                    if (var9_9 == 0 || f.a(var7_7 + var9_9 >> 14, var8_8 >> 14, var5_5, var6_6, var0.L == 0)) break block24;
                    if (var2_2) {
                        var0.g[var4_4 + 11] = var11_11;
                        var0.g[var4_4 + 12] = 0;
                    }
                    var0.a.a = var7_7 + var9_9;
                    v3 = var0.a;
                    v4 = var8_8;
                    break block25;
                }
                if (var10_10 == 0 || f.a(var7_7 >> 14, var8_8 + var10_10 >> 14, var5_5, var6_6, var0.L == 0)) break block26;
                if (var2_2) {
                    var0.g[var4_4 + 11] = 0;
                    var0.g[var4_4 + 12] = var12_12;
                }
                var0.a.a = var7_7;
                v3 = var0.a;
                v4 = var8_8 + var10_10;
            }
            v3.b = v4;
            var3_3 = true;
        }
        g.a(var0, 0, true);
        return var3_3;
    }

    /*
     * Enabled force condition propagation
     * Lifted jumps to return sites
     */
    public static int a(f f2, boolean bl) {
        int n = 0;
        int n2 = f.d(f2);
        int n3 = n2 + 11;
        int n4 = n2 + 12;
        if (!bl) {
            if (f2.g[n3] == 0) {
                if (f2.g[n4] == 0) return n;
            }
            if (f2.g[n3] > 8192) {
                return 3;
            }
            if (f2.g[n3] < -8192) {
                return 2;
            }
            if (f2.g[n4] > 8192) {
                return 1;
            }
        } else {
            int n5;
            int n6 = g.f(20) << 6;
            int n7 = g.e(20) << 6;
            int n8 = -n7;
            int n9 = -n6;
            int n10 = n6;
            int n11 = n7;
            if (f2.g[n3] < n8) {
                return 4;
            }
            if (f2.g[n3] < n9) {
                n5 = 1;
            } else if (f2.g[n3] < n10) {
                n5 = 2;
            } else {
                if (f2.g[n3] >= n11) return 0;
                n5 = 3;
            }
            int n12 = n5;
            if (n5 == 0) {
                return 4;
            }
            if (n12 == 1) {
                if (f2.g[n4] >= 0) return 5;
                return 3;
            }
            if (n12 == 2) {
                if (f2.g[n4] >= 0) return 6;
                return 2;
            }
            if (n12 != 3) return 0;
            if (f2.g[n4] >= 0) return 7;
            return 1;
        }
        if (f2.g[n4] >= -8192) return n;
        return 0;
    }

    private static boolean a(int n, int n2, boolean bl, boolean bl2, boolean bl3) {
        int n3 = 13;
        if (bl2) {
            n3 = 77;
        }
        boolean bl4 = true;
        if (bl) {
            int n4 = 16;
            if (bl3) {
                n4 = 32;
            }
            boolean bl5 = bl4 = (g.f(g.b(n), g.b(n2)) & n4) != 0;
        }
        return !bl4 || g.a(g.b(n), g.b(n2), n3) || g.a(g.b(n - 5), g.b(n2 + 4), n3) || g.a(g.b(n + 4), g.b(n2 + 4), n3) || g.a(g.b(n - 5), g.b(n2 - 5), n3) || g.a(g.b(n + 4), g.b(n2 - 5), n3);
    }

    public static boolean i(f f2) {
        return f2.g[25] >= 555;
    }

    public static void r(f f2) {
        int n = f.e(f2);
        if (n != 3 && n != 0) {
            int n2 = f.a(f2, f2.L != 1);
            if (f2.L == 1) {
                n2 += 0;
            } else {
                n2 += 64;
                n2 += f.a();
            }
            if (n2 >= 0 && f2.a.d != n2) {
                f2.a.b(n2);
            }
        }
    }

    /*
     * Unable to fully structure code
     */
    public static void s(f var0) {
        if (var0.L == 0) {
            return;
        }
        var1_1 = var0.a.d % 4;
        if (var0.a.d >= 22 && var0.a.d <= 25) {
            var1_1 = g.d(var0.a.d - 22) % 4;
        }
        var2_2 = f.d(var0);
        switch (var1_1) {
            case 0: {
                var0.g[var2_2 + 11] = 0;
                v0 = var0.g;
                v1 = var2_2 + 12;
                v2 = -16384;
                ** GOTO lbl33
            }
            case 1: {
                var0.g[var2_2 + 11] = 0;
                v0 = var0.g;
                v1 = var2_2 + 12;
                v2 = 16384;
                ** GOTO lbl33
            }
            case 2: {
                v3 = var0.g;
                v4 = var2_2 + 11;
                v5 = -16384;
                ** GOTO lbl29
            }
            case 3: {
                v3 = var0.g;
                v4 = var2_2 + 11;
                v5 = 16384;
lbl29:
                // 2 sources

                v3[v4] = v5;
                v0 = var0.g;
                v1 = var2_2 + 12;
                v2 = 0;
lbl33:
                // 3 sources

                v0[v1] = v2;
            }
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void ad(f var0) {
        block34: {
            block33: {
                var1_1 = f.a(var0, false);
                var2_2 = f.d(var0);
                var4_3 = var0.g[var2_2 + 1];
                var5_4 = false;
                if (var0.L != 1) break block33;
                switch (var4_3) {
                    case 0: {
                        if (f.B(var0)) {
                            v0 = var2_2 + 13;
                            var0.g[v0] = var0.g[v0] + (int)g.d;
                        }
                        if (var0.g[var2_2 + 13] < 5000) break;
                        var5_4 = true;
                        break;
                    }
                    default: {
                        var0.g[var2_2 + 13] = 0;
                    }
                }
                switch (var4_3) {
                    case 3: 
                    case 6: 
                    case 7: {
                        var1_1 += 4;
                        break;
                    }
                    case 1: 
                    case 5: {
                        var1_1 += 8;
                        break;
                    }
                    case 0: 
                    case 4: 
                    case 8: {
                        if (var5_4) {
                            var1_1 = 16;
                            break;
                        }
                        var1_1 += 0;
                        break;
                    }
                    case 100: {
                        var1_1 = 19;
                        break;
                    }
                    case 101: {
                        var1_1 = 20;
                        break;
                    }
                    case 102: 
                    case 555: 
                    case 666: {
                        var1_1 += 12;
                        break;
                    }
                    case 556: 
                    case 667: {
                        var1_1 += 22;
                        break;
                    }
                    case 104: {
                        var1_1 += 29;
                    }
                }
                break block34;
            }
            var6_5 = 0;
            var2_2 = 29;
            var7_6 = g.a(var0.g[43], 65280);
            var4_3 = var0.g[30];
            switch (var4_3) {
                case 3: 
                case 6: 
                case 7: {
                    var6_5 = 1;
                    var1_1 += 76;
                    break;
                }
                case 1: 
                case 5: {
                    if (var7_6 == 255) {
                        var6_5 = 1;
                        var1_1 += 72;
                        break;
                    }
                    v1 = g.a(var0, var7_6, 3) + f.a(var0, true);
                    break;
                }
                case 0: 
                case 4: 
                case 8: {
                    if (var7_6 == 255) {
                        var6_5 = 1;
                        v1 = 64 + f.a(var0, true);
                        break;
                    }
                    v1 = g.a(var0, var7_6, 2) + f.a(var0, true);
                    break;
                }
                case 100: {
                    var1_1 += 8;
                    break;
                }
                case 101: {
                    var1_1 += 12;
                    break;
                }
                case 102: 
                case 555: 
                case 666: {
                    v1 = 7;
                    break;
                }
                case 104: {
                    break;
                }
                case 103: {
                    v2 = var0;
                    v3 = 8;
                    ** GOTO lbl86
                }
                case 9: {
                    v2 = var0;
                    v3 = 6;
lbl86:
                    // 2 sources

                    v1 = var1_1 = f.a(v2, v3, f.a(var0, true), 0, var0.g[28], var0.g[29]);
                }
            }
            if (var6_5 != 0) {
                var1_1 += f.a();
                var1_1 += g.k(var0.g[28]);
            }
        }
        if (var1_1 >= 0 && var0.a.d != var1_1) {
            if ((var0.g[var2_2 + 14] & 1) != 0) {
                var6_5 = g.a(var0.g[var2_2 + 14], 0xF000000);
                if (var6_5 >= 3) {
                    var0.a.b(var1_1);
                    var0.g[var2_2 + 14] = g.a(var0.g[var2_2 + 14], 0xF000000, 0);
                    return;
                }
                var0.g[var2_2 + 14] = g.a(var0.g[var2_2 + 14], 0xF000000, ++var6_5);
                return;
            }
            var0.a.b(var1_1);
            var0.g[var2_2 + 14] = g.a(var0.g[var2_2 + 14], 0xF000000, 0);
            if (var5_4) {
                var0.a.e = g.a() % var0.a.a.a(var0.a.d);
            }
        }
    }

    public static boolean j(f f2) {
        int n = 10;
        if (f2.L == 0) {
            n = 7;
        }
        return f2.g[n] != 0;
    }

    public static void e(f f2, int n) {
        if (f.m(f2) < 555) {
            if (f2.L == 0) {
                return;
            }
            if (f2.g[10] > 0) {
                f2.g[10] = f2.g[10] - n;
                if (f2.g[10] <= 0) {
                    f2.g[10] = 0;
                }
                if (f.e(f2) == 3) {
                    f.m(f2, 1);
                }
            }
        }
    }

    private static void o(f f2, int n) {
        if (f.m(f2) < 555) {
            f.e(f2, n);
            int n2 = 10;
            if (f2.L == 0) {
                n2 = 7;
            }
            if (f2.g[n2] == 0) {
                f.d(f2, 555);
            }
        }
    }

    private static void e(Graphics graphics, f f2) {
        int n;
        f2.a.a.e = f2.g[2];
        int n2 = -1;
        if (f2.L == 0 || f2.g[11] != 0) {
            n2 = 0;
        }
        if (n2 >= 0) {
            f.a(graphics, n2, f2.a.a >> 14, f2.a.b >> 14);
        }
        if (f2.g[(n = f.d(f2)) + 1] == 556) {
            f2.a.a(graphics);
        }
        int n3 = g.a(f2);
        f2.a.a.a(n3);
        f2.a.a(graphics);
        if (g.h[0][0] != 0 && f2.L == 1 && (f2.g[17] == 2 || f2.g[17] == 4)) {
            int[] nArray = g.a(f2.a);
            int n4 = nArray[3] - nArray[1];
            int n5 = 11;
            if ((f2.g[n + 14] & 2) == 0 && g.I) {
                n5 = 12;
            }
            a a2 = g.a[12];
            a2.a(graphics, n5, f2.a.a(), f2.a.b() - n4, 0);
        }
        if (g.g > 0) {
            graphics.setColor(0xFF0000);
            g.a(graphics, f2.a.a(), f2.a.b());
        }
    }

    public static int[] d(int[] nArray) {
        int n;
        int n2;
        int[] nArray2;
        int[] nArray3 = null;
        if (nArray != null) {
            nArray3 = new int[nArray.length + 3];
            System.arraycopy((Object)nArray, (int)0, (Object)nArray3, (int)0, (int)nArray.length);
            nArray3[0] = g.a(g.w, nArray3[0]);
        } else {
            nArray3 = new int[4];
        }
        for (int i = 0; i < 3; ++i) {
            nArray3[4 + i] = 0;
        }
        if (nArray == null) {
            nArray2 = nArray3;
            n2 = 4;
            n = -1;
        } else {
            nArray3[4] = 0;
            nArray2 = nArray3;
            n2 = 5;
            n = g.k(nArray3[0], 8);
        }
        nArray2[n2] = n;
        return nArray3;
    }

    private static void ae(f f2) {
        f2.a.a();
        if (f2.g[4] != -1) {
            switch (f2.g[4]) {
                case 0: {
                    break;
                }
                case 2: {
                    if (!f2.a.a()) break;
                    f.b(f2, true);
                    break;
                }
                case 1: {
                    if (!f2.a.a()) break;
                    int n = g.k(f2.g[0], 6);
                    int n2 = g.k(f2.g[0], 7);
                    int n3 = f2.a.a() + (n * 16 >> 1);
                    int n4 = f2.a.b() + (n2 * 16 >> 1);
                    int n5 = g.k(f2.g[0], 9) << 14;
                    int n6 = g.k(f2.g[0], 10);
                    g.a(n3, n4, 0, n5, n6, true);
                    f.b(f2, true);
                    break;
                }
                case 3: {
                    break;
                }
                default: {
                    g.n(f2);
                }
            }
        }
        f.af(f2);
    }

    public static void b(f f2, boolean bl) {
        f2.g[5] = 0;
        f2.g[4] = 3;
        g.d(f2);
        g.c(f2);
        if (bl) {
            int n;
            boolean bl2 = false;
            int n2 = 16 * g.k(f2.g[0], 6);
            int n3 = 16 * g.k(f2.g[0], 7);
            int n4 = f2.a.a() + (n2 >> 1);
            if (!g.b(n4 / 16, (n = f2.a.b() + (n3 >> 1)) / 16, 5)) {
                bl2 = true;
            }
            if (!bl2 && g.a(g.s, f2.a.a() / 16, f2.a.b() / 16, (f2.a.a() + n2 - 1) / 16, (f2.a.b() + n3 - 1) / 16, 5)) {
                bl2 = true;
                n4 = g.s[0] * 16 + 8;
                n = g.s[1] * 16 + 8;
            }
            if (!bl2) {
                n4 = f2.a.a();
                n = f2.a.b();
            }
            g.b(f2.g[3], n4 << 14, n << 14);
        }
        g.k(f2);
    }

    public static boolean a(f f2, int n) {
        return f.a(g.l(n), f2);
    }

    private static void af(f f2) {
        int n;
        int n2 = 0;
        switch (f2.g[4]) {
            case 0: {
                n = g.k(f2.g[0], 3);
                break;
            }
            case 1: 
            case 2: {
                n = g.k(f2.g[0], 5);
                break;
            }
            case 3: {
                n = g.k(f2.g[0], 4);
                break;
            }
            default: {
                n = n2 = -1;
            }
        }
        if (n >= 0 && f2.a.d != n2) {
            f2.a.b(n2);
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void a(int var0, int var1_1, f var2_2, int var3_3, int var4_4) {
        switch (var2_2.L) {
            case 9: {
                if (var2_2.g[4] != 0) break;
                f.a(var1_1, var2_2);
                return;
            }
            case 3: {
                if (var2_2.g[12] == -1) break;
                f.G(var2_2);
                f.a(var2_2, var0, var1_1, var3_3 << 14, var4_4 << 14);
                return;
            }
            case 0: {
                if (var2_2 == g.c) {
                    f.a(var2_2, var1_1, true);
                    return;
                }
                v0 = var2_2;
                ** GOTO lbl20
            }
            case 1: {
                v0 = var2_2;
lbl20:
                // 2 sources

                f.e(v0, var1_1);
                f.g(var2_2, var3_3 << 14, var4_4 << 14, 1);
                f.d(var2_2, 102);
            }
        }
    }

    public static void a(int n, int n2, int n3, int n4, f f2) {
        int n5;
        int n6 = 0;
        int n7 = 0;
        if (f2.L == 9) {
            n6 = g.k(f2.g[0], 6) << 4 >> 1;
            n7 = g.k(f2.g[0], 7) << 4 >> 1;
        }
        if ((n5 = g.a(n, n2, f2.a.a() + n6, f2.a.b() + n7)) >= 0 && n5 <= n4) {
            int n8 = n3 - n3 / n4 * n5 >> 14;
            f.a(n3 >> 14, n8, f2, n, n2);
        }
    }

    public static void a(int n, int n2, int n3, int n4, f[] fArray) {
        for (int i = 0; i < fArray.length; ++i) {
            f.a(n, n2, n3, n4, fArray[i]);
        }
    }

    public static boolean k(f f2) {
        int n = g.k(f2.g[0], 8);
        return f.a(n, f2);
    }

    public static boolean a(int n, f f2) {
        if (f2.g[4] < 100) {
            if (f2.g[5] > 0) {
                int n2 = g.k(f2.g[0], 12);
                if (n >= n2) {
                    f2.g[5] = f2.g[5] - n;
                }
                if (f2.g[5] <= 0) {
                    int n3;
                    int n4;
                    int[] nArray;
                    f2.g[5] = 0;
                    int n5 = g.k(f2.g[0], 9);
                    if (n5 > 0) {
                        nArray = f2.g;
                        n4 = 4;
                        n3 = 1;
                    } else {
                        nArray = f2.g;
                        n4 = 4;
                        n3 = 2;
                    }
                    nArray[n4] = n3;
                    f.af(f2);
                }
                return true;
            }
        } else {
            g.m(f2);
        }
        return false;
    }

    private static void f(Graphics graphics, f f2) {
        int n;
        if (f2.g[4] == 3 && (n = g.k(f2.g[0], 13)) >= 0) {
            g.e[f2.g[0]].a = f2.a.a;
            g.e[f2.g[0]].b = f2.a.b;
            g.e[f2.g[0]].a();
            g.e(16);
            g.e[f2.g[0]].a();
            g.e[f2.g[0]].a(graphics);
            g.f(16);
        }
        f2.a.a(graphics);
    }

    public static void t(f f2) {
        if (f2.g[4] == 3) {
            k = true;
        }
    }

    public static boolean l(f f2) {
        int n = g.k(f2.g[0], 9);
        return f2.g[4] == 3 && n > 0;
    }

    public static int[] a(f f2) {
        return g.a(g.a[18], 18, f2.a.a(), f2.a.b(), 0);
    }

    public static void a(Graphics graphics, f f2, boolean bl) {
        if (f2.g[4] == 3) {
            int n = f2.a.a - g.T >> 14;
            int n2 = (f2.a.b - g.U >> 14) - 0;
            int n3 = g.k(f2.g[0], 9);
            if (n3 > 0) {
                g.a[18].a(graphics, 18, n, n2, 0);
            }
            if (n3 > 0) {
                int[] nArray = g.a(g.a[18], 18, f2.a.a(), f2.a.b(), 0);
                g.a(graphics, nArray, nArray[3], true);
            }
        }
    }

    public static void u(f f2) {
        int n;
        f f3;
        int n2 = g.k(f2.g[0], 6) << 4;
        int n3 = g.k(f2.g[0], 7) << 4;
        if (f2.g[4] == 3) {
            f3 = f2;
            n = f2.a.b();
        } else {
            f3 = f2;
            n = f2.a.b() + n3 - 1;
        }
        f3.M = (n << 8) + f2.a.a() + (n2 >> 1);
    }

    public static int[] e(int[] nArray) {
        int[] nArray2 = new int[nArray.length + 2];
        System.arraycopy((Object)nArray, (int)0, (Object)nArray2, (int)0, (int)nArray.length);
        nArray2[6] = -1;
        return nArray2;
    }

    public static void v(f f2) {
        int n = f2.a.a() + f2.g[0];
        int n2 = f2.a.b() + f2.g[1];
        f2.M = (n2 << 8) + n;
    }

    public static void f(f f2, int n) {
        f2.g[4] = n;
        int n2 = f2.a.a() / 16;
        int n3 = (f2.a.a() + f2.g[0]) / 16;
        int n4 = f2.a.b() / 16;
        int n5 = (f2.a.b() + f2.g[1]) / 16;
        for (int i = 0; i < g.cg; ++i) {
            int n6;
            int n7;
            int n8;
            f f3 = g.e[i];
            if (f3.L != 3 || (n8 = g.h(f3.g[0], 10)) != 5 && n8 != 7 || !g.b(n2, n4, n3, n5, n7 = f3.a.a() / 16, n6 = f3.a.b() / 16, n7, n6)) continue;
            if (n != 0) {
                f.D(f3);
            }
            if (g.b == 0) continue;
            f.C(f3);
        }
    }

    private static void p(f f2, int n) {
        f2.g[7] = n;
        for (int i = 0; i < f2.g[3]; ++i) {
            f f3 = g.j[g.by][g.bz][f2.g[6] + i];
            int n2 = f3.g[12];
            if (!(f3.g[12] >= 100 || f3.g[12] == -1 && (f3.g[16] & 0x40) != 0 || f.s(f3))) {
                int n3;
                switch (n) {
                    case 2: {
                        n3 = 4;
                        break;
                    }
                    case 1: {
                        n3 = 0;
                        break;
                    }
                    case 3: {
                        n3 = -1;
                        break;
                    }
                    default: {
                        n3 = -1;
                    }
                }
                n2 = n3;
            }
            f.c(f3, n2);
        }
    }

    private static void ag(f f2) {
        g.b(f2.a.a(), f2.a.b(), f2.g[0], f2.g[1], f2.g[6], f2.g[3]);
    }

    private static boolean d(f f2, f f3) {
        int n = f3.a.a() / 16;
        int n2 = f3.a.b() / 16;
        int n3 = f2.a.a();
        int n4 = f2.a.b();
        int n5 = f2.g[0];
        int n6 = f2.g[1];
        int n7 = n3 / 16;
        int n8 = (n3 + n5 - 1) / 16;
        int n9 = n4 / 16;
        int n10 = (n4 + n6 - 1) / 16;
        return g.b(n, n2, n, n2, n7, n9, n8, n10);
    }

    private static f d(f f2) {
        int n;
        f f3 = null;
        for (n = 0; n < g.c.length && f3 == null; ++n) {
            if (!f.b(5, g.c[n]) || !f.d(f2, g.c[n])) continue;
            f3 = g.c[n];
        }
        for (n = 0; n < g.f[g.by][g.bz].length && f3 == null; ++n) {
            if (!f.b(5, g.f[g.by][g.bz][n]) || !f.d(f2, g.f[g.by][g.bz][n])) continue;
            f3 = g.f[g.by][g.bz][n];
        }
        return f3;
    }

    private static void e(f f2, f f3) {
        for (int i = 0; i < f2.g[3]; ++i) {
            f f4 = g.j[g.by][g.bz][f2.g[6] + i];
            if (f4.g[12] >= 100) continue;
            if (f3 == null) {
                f.i(f4);
            }
            f.d(f4, f3);
        }
    }

    private static void ah(f f2) {
        block8: {
            int n;
            f f3;
            block7: {
                block5: {
                    f f4;
                    block6: {
                        if (f2.g[5] == 0) break block5;
                        if (f2.g[7] == 0) {
                            f.ag(f2);
                            f.p(f2, 1);
                        }
                        if (f2.g[7] == 3) {
                            f.p(f2, 1);
                        }
                        if ((f4 = f.d(f2)) == null || f2.g[7] != 1) break block6;
                        f.e(f2, f4);
                        f3 = f2;
                        n = 2;
                        break block7;
                    }
                    if (f4 != null || f2.g[7] != 2) break block8;
                    f.e(f2, null);
                    f3 = f2;
                    n = 1;
                    break block7;
                }
                if (f2.g[7] == 3 || f2.g[7] == 0) break block8;
                f3 = f2;
                n = 3;
            }
            f.p(f3, n);
        }
    }

    public static f[] a(f f2) {
        return g.a(f2.a.a(), f2.a.b(), f2.g[3], 174, 3, 2, 16);
    }

    public f(int n, int[] nArray) {
        this.a = new c(null, 0, 0, null);
        this.L = n;
        this.g = nArray;
    }

    public f(c c2, int n, int n2, int[] nArray) {
        this.a = c2;
        this.K = n;
        this.L = n2;
        this.g = nArray;
        this.M = (this.a.b() << 8) + this.a.a();
    }

    public f(int n, int n2, int n3, int n4, int[] nArray) {
        this.K = n;
        this.L = n2;
        this.g = nArray;
        this.a = new c(null, n3, n4, null);
        if (n2 < 9) {
            switch (n2) {
                case 0: {
                    this.a.b(66);
                    return;
                }
                case 3: {
                    this.a.b(g.h(this.g[0], 2));
                    return;
                }
            }
            this.a.b(this.g[5]);
            return;
        }
        if (n2 < 20) {
            switch (n2) {
                case 16: {
                    this.a.b(this.g[2]);
                    return;
                }
                case 15: {
                    this.a.a(g.a[g.x[this.g[3]]]);
                    if (this.g[0] >= 0) {
                        g.a(this.a, this.g[0]);
                        return;
                    }
                    this.a.b(this.g[1]);
                    return;
                }
                case 12: {
                    return;
                }
                case 9: {
                    this.a.b(g.k(this.g[0], 3));
                    return;
                }
                case 18: {
                    this.a.a(g.a[16]);
                    return;
                }
                case 26: {
                    this.a.b(this.g[2]);
                    return;
                }
            }
            if (this.g[4] >= 0) {
                g.a(this.a, this.g[4]);
                return;
            }
            this.a.b(this.g[5]);
            return;
        }
        if (n2 == 21) {
            f.b(this.g);
        }
    }

    public final void g() {
        if (this.a != null) {
            if (this.a.a != null) {
                this.a.a.b();
                this.a.a = null;
            }
            this.a = null;
        }
        this.g = null;
    }

    public final void a(a a2) {
        if (this.a != null && a2 != null) {
            this.a.a(a2);
        }
    }

    public final void h() {
        switch (this.L) {
            case 0: {
                f.a(this.a);
                return;
            }
            case 20: 
            case 21: 
            case 22: 
            case 23: 
            case 24: 
            case 25: {
                f.a(this.L, this.g, this.a.a(), this.a.b());
                return;
            }
            case 14: {
                g.a(this);
                return;
            }
            case 18: {
                f.ah(this);
                return;
            }
            case 9: {
                f.ae(this);
                return;
            }
            case 1: {
                f.q(this);
                return;
            }
            case 3: {
                f.a(this, true);
                return;
            }
        }
        this.a.a();
    }

    public static void a(Graphics graphics, int n, int n2, int n3) {
        g.a[13].a(graphics, n, n2, n3, 0);
        int[] nArray = g.a(g.a[13], n);
        int[] nArray2 = nArray;
        nArray[0] = nArray[0] + (n2 + (g.T >> 14));
        nArray2[1] = nArray2[1] + (n3 + (g.U >> 14) - 0);
        nArray2[2] = nArray2[2] + (n2 + (g.T >> 14));
        nArray2[3] = nArray2[3] + (n3 + (g.U >> 14) - 0);
        g.a(graphics, nArray2, n3, true);
    }

    /*
     * Enabled force condition propagation
     * Lifted jumps to return sites
     */
    private boolean a(Graphics graphics, boolean bl) {
        boolean bl2 = false;
        switch (this.L) {
            case 0: 
            case 1: {
                if (this == g.c) {
                    f.c(graphics, this);
                    return true;
                } else {
                    f.e(graphics, this);
                }
                return true;
            }
            case 3: {
                f.e(graphics, this, bl);
                return true;
            }
            case 14: {
                g.a(graphics, this);
                return true;
            }
            case 9: {
                f.f(graphics, this);
                return true;
            }
            case -101: {
                g.d(graphics, this);
                return true;
            }
            case 18: {
                return true;
            }
            case 26: {
                g.c(graphics, this);
                return true;
            }
            case 22: {
                f.b(graphics, this.g, this.a.a(), this.a.b());
                return bl2;
            }
            case -100: {
                if (this.g[0] != 4) return bl2;
                g.b(graphics, this);
                return true;
            }
        }
        return bl2;
    }

    /*
     * Unable to fully structure code
     */
    public final void a(Graphics var1_1, boolean var2_2) {
        block12: {
            block13: {
                block15: {
                    block14: {
                        if (this.a == null || this.a.a == null && this.L != 16 && this.L != 22) break block12;
                        var4_3 = this.a.a;
                        var5_4 = this.a.b;
                        this.a.a -= g.T >> 14 << 14;
                        this.a.b -= (g.U >> 14) - 0 << 14;
                        if (this.a(var1_1, var2_2)) break block13;
                        if (this.L == -100) {
                            this.a.a.e = this.g[9];
                            this.a.a.a(this.g[10]);
                            this.a.b += this.g[6];
                        }
                        if (this.L != 15) break block14;
                        switch (this.g[2]) {
                            case 1: {
                                v0 = 8;
                                ** GOTO lbl18
                            }
                            case 2: {
                                v0 = 16;
lbl18:
                                // 2 sources

                                g.e(v0);
                            }
                        }
                        this.a.a(var1_1);
                        g.f(24);
                        break block15;
                    }
                    this.a.a(var1_1);
                }
                switch (this.L) {
                    case -100: {
                        g.a(var1_1, this.g[8]);
                        break;
                    }
                    case 16: {
                        if (this.g[24] != 1 || (this.g[28] & 8) != 0 || (var6_5 = this.g[21]) < 0) break;
                        var7_7 = g.b[var6_5][2];
                        if (var7_7 != g.a.d) {
                            g.a.b(var7_7);
                        }
                        g.a.a = this.a.a;
                        g.a.b = this.a.b;
                        g.a.a(var1_1);
                    }
                }
            }
            this.a.a += g.T >> 14 << 14;
            this.a.b += (g.U >> 14) - 0 << 14;
            if (!(this.L == 10 && this.g[7] != 0 || this.L == 3 && this.g[10] == 4)) {
                var6_6 = f.d(this);
                var7_7 = 0;
                var8_8 = 0;
                if (this.L == -101) {
                    var7_7 = g.a(this.g[15], 255);
                    var8_8 = g.l(var7_7, 21);
                }
                var9_9 = this.L == 0 || this.L == 3 || this.L == 1 || this.L == -100 && this.g[0] == 3 || this.L == 9 || this.L == 14 && this.g[16] != -1 || this.L == -101 && var8_8 != 0 && (this.g[0] == 5 || this.g[0] == 3 && this.g[1] == 3) || this.L == -200;
                g.a(var1_1, var6_6, f.p(this), var9_9);
            }
            this.a.a = var4_3;
            this.a.b = var5_4;
        }
    }

    /*
     * Unable to fully structure code
     */
    private static int p(f var0) {
        var1_1 = var0.a.b;
        var2_2 = null;
        switch (var0.L) {
            case 14: {
                v0 = var1_1;
                v1 = var0.g[12] << 14;
                ** GOTO lbl66
            }
            case 3: {
                var3_3 = g.h(var0.g[0], 10);
                block6 : switch (var3_3) {
                    case 2: {
                        switch (var0.g[12]) {
                            case 7: {
                                v2 = var1_1;
                                v3 = g.k[var0.g[28]].g;
                                v4 = 10;
                                ** GOTO lbl26
                            }
                            case 8: {
                                var7_4 = g.c.a.a.a(0, var0.g[27]);
                                v5 = var1_1 - (var7_4[1] + (var7_4[3] >> 1) << 14);
                                ** GOTO lbl27
                            }
                            case 9: {
                                v2 = var1_1;
                                v3 = var0.g;
                                v4 = 28;
lbl26:
                                // 2 sources

                                v5 = v2 + v3[v4];
lbl27:
                                // 2 sources

                                var1_1 = v5;
                            }
                        }
                        break;
                    }
                    case 1: {
                        var2_2 = g.b(var0.a);
                        var4_6 = g.b(var2_2[3] - (var1_1 >> 14)) + 1;
                        var5_7 = g.b(var0.a.a());
                        var6_8 = g.b(var0.a.b());
                        for (var7_5 = 0; var7_5 < var4_6; ++var7_5) {
                            if (g.b(var5_7 - 1, var6_8, 2) || g.b(var5_7, var6_8, 2) || g.b(var5_7 + 1, var6_8, 2)) {
                                var1_1 = var2_2[3] << 14;
                                break block6;
                            }
                            ++var6_8;
                        }
                        break;
                    }
                }
                break;
            }
            case -101: {
                if (var0.g[0] != 5) break;
                var1_1 = var0.g[5];
                switch (var0.g[15]) {
                    case 0: 
                    case 4: {
                        v6 = var0;
                        ** GOTO lbl58
                    }
                    case 6: {
                        v7 = var1_1 - 131072;
                        ** GOTO lbl59
                    }
                    case 1: 
                    case 2: 
                    case 3: {
                        if (g.a(var0.a.a, var0.a.b, var0.g[4] + var0.g[9], var0.g[5] + var0.g[10], g.s, false, 1)) {
                            v7 = g.s[1] + 262144;
                        } else {
                            v6 = var0;
lbl58:
                            // 2 sources

                            v7 = v6.a.b;
                        }
lbl59:
                        // 3 sources

                        var1_1 = v7;
                    }
                }
                break;
            }
            case -200: {
                var2_2 = g.b(var0.a);
                if (!g.a(var0.a.a, var0.a.b, var0.a.a, var2_2[3] << 14, g.s, false, 1)) break;
                v0 = g.s[1];
                v1 = 262144;
lbl66:
                // 2 sources

                var1_1 = v0 + v1;
            }
        }
        return var1_1 >> 14;
    }

    /*
     * Unable to fully structure code
     */
    private static int[] d(f var0) {
        block17: {
            block14: {
                block16: {
                    block15: {
                        var1_1 = g.b(var0.a);
                        if (var0.L != 3 || g.h(var0.g[0], 34) == -1) break block14;
                        var2_2 = var1_1[0];
                        var3_3 = var1_1[1];
                        var4_4 = var1_1[2];
                        var5_5 = var1_1[3];
                        if ((var0.g[16] & 4096) == 0) break block15;
                        var1_1 = g.a(var0.a.a, f.g(var0), var0.a.a(), var0.a.b(), 0);
                        if (var1_1[0] > var2_2) {
                            var1_1[0] = var2_2;
                        }
                        if (var1_1[1] > var3_3) {
                            var1_1[1] = var3_3;
                        }
                        if (var1_1[2] < var4_4) {
                            var1_1[2] = var4_4;
                        }
                        if (var1_1[3] >= var5_5) break block14;
                        break block16;
                    }
                    var1_1 = g.a(var0.a.a, g.i(var0.g[0], 14));
                    var6_6 = var1_1[3] - var1_1[1];
                    var1_1[0] = var2_2;
                    var1_1[1] = var3_3 - var6_6;
                    var1_1[2] = var4_4;
                }
                var1_1[3] = var5_5;
            }
            if (var0.L == 3 && var1_1 != null) {
                var2_2 = f.b[0];
                var3_3 = f.b[1];
                var4_4 = f.b[2];
                var5_5 = f.b[3];
                if (!f.f()) {
                    var2_2 += g.T >> 14;
                    var3_3 += g.U >> 14;
                    var4_4 += g.T >> 14;
                    var5_5 += g.U >> 14;
                }
                if (var2_2 < var1_1[0]) {
                    var1_1[0] = var2_2;
                }
                if (var4_4 > var1_1[2]) {
                    var1_1[2] = var4_4;
                }
                if (var3_3 < var1_1[1]) {
                    var1_1[1] = var3_3;
                }
                if (var5_5 > var1_1[3]) {
                    var1_1[3] = var5_5;
                }
            }
            if (var0.L != -101) break block17;
            switch (var0.g[0]) {
                case 5: {
                    var1_1[0] = (Math.min((int)var0.g[4], (int)var0.g[2]) >> 14) - 16;
                    var1_1[1] = (Math.min((int)var0.g[5], (int)var0.g[3]) >> 14) - 16;
                    var1_1[2] = (Math.max((int)var0.g[4], (int)var0.g[2]) >> 14) + 16;
                    v0 = var1_1;
                    v1 = 3;
                    v2 = Math.max((int)var0.g[5], (int)var0.g[3]) >> 14;
                    v3 = 16;
                    ** GOTO lbl72
                }
                case 4: {
                    var1_1[1] = var1_1[1] - (var0.g[10] >> 14);
                    v1 = 3;
                    v0 = var1_1;
                    v4 = var1_1[3] - (var0.g[10] >> 14);
                    ** GOTO lbl73
                }
                case 3: {
                    if (var0.g[1] != 3 || (var3_3 = g.l(var2_2 = g.a(var0.g[15], 255), 21)) == 0) break;
                    var4_4 = var0.a.a() - (var0.g[9] >> 14);
                    var5_5 = var0.a.b() - (var0.g[10] >> 14);
                    var1_1[0] = var4_4 - 32;
                    var1_1[1] = var5_5 - 32;
                    var1_1[2] = var4_4 + 32;
                    v0 = var1_1;
                    v1 = 3;
                    v2 = var5_5;
                    v3 = 32;
lbl72:
                    // 2 sources

                    v4 = v2 + v3;
lbl73:
                    // 2 sources

                    v0[v1] = v4;
                }
            }
        }
        return var1_1;
    }

    static {
        e = -1;
        f = -1;
        h = 2304;
        n = 1;
        o = 1;
        a = null;
        b = false;
        c = false;
        d = false;
        z = -1;
        a = null;
        a = null;
        a = null;
        b = null;
        c = g.r;
        d = null;
        a = null;
        b = null;
        f = false;
        g = false;
        h = false;
        i = false;
        e = new int[2];
        c = null;
        J = -1;
        f = null;
        j = false;
        k = false;
    }
}
