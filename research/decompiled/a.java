/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  java.lang.Exception
 *  java.lang.Object
 *  java.lang.System
 *  javax.microedition.lcdui.Graphics
 *  javax.microedition.lcdui.Image
 */
import javax.microedition.lcdui.Graphics;
import javax.microedition.lcdui.Image;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public final class a {
    public static Graphics a;
    public static final int[] a;
    public static int a;
    public static byte[] a;
    public int b;
    public static int[] b;
    public int c;
    public short[] a;
    public short[] b;
    public short[] c;
    public short[] d;
    public byte[] b;
    public short[] e;
    public byte[] c;
    public short[] f;
    public short[] g;
    public byte[] d;
    public byte[] e;
    public short[] h;
    public byte[] f;
    public byte[] g;
    public short[] i;
    public short[] j;
    public byte[] h;
    public byte[][] a;
    public short[] k;
    public byte[] i;
    public int d;
    public short[][] a;
    public int e;
    public int f;
    public int[][] a;
    public int g;
    public int h;
    public int i;
    public boolean a;
    public short a;
    public int j;
    public int k;
    public byte[] j;
    public int[] c;
    public Image[][] a;
    public int[][][] a;
    public int[] d;
    public static int l;
    public static int m;
    public static int n;
    public static int o;
    public static int p;
    public byte[] k;
    public int[] e;

    public final void a(byte[] byArray, int n) {
        int n2;
        int n3;
        int n4;
        int n5;
        int n6;
        int n7;
        int n8;
        int n9;
        int n10;
        ++n;
        int n11 = ++n;
        int n12 = ++n;
        int n13 = ++n;
        int n14 = ++n;
        this.f = (byArray[n11] & 0xFF) + ((byArray[n12] & 0xFF) << 8) + ((byArray[n13] & 0xFF) << 16) + ((byArray[n14] & 0xFF) << 24);
        int n15 = ++n;
        int n16 = ++n;
        ++n;
        this.c = (byArray[n15] & 0xFF) + ((byArray[n16] & 0xFF) << 8);
        if (this.c > 0) {
            this.a = new short[this.c];
            this.b = new short[this.c];
            this.c = new short[this.c];
            this.d = new short[this.c];
            this.k = new byte[this.c];
            this.e = new int[this.c];
            for (n10 = 0; n10 < this.c; ++n10) {
                int n17;
                int n18;
                short[] sArray;
                if ((n9 = byArray[n++] & 0xFF) == 255) {
                    this.k[n10] = 1;
                    this.e[n10] = (byArray[n] & 0xFF) + ((byArray[n + 1] & 0xFF) << 8) + ((byArray[n + 2] & 0xFF) << 16) + ((byArray[n + 3] & 0xFF) << 24);
                    n += 4;
                    this.c[n10] = (short)(byArray[n++] & 0xFF);
                    sArray = this.d;
                    n18 = n10;
                    n17 = byArray[n++] & 0xFF;
                } else if (n9 == 254) {
                    this.k[n10] = 2;
                    this.e[n10] = (byArray[n] & 0xFF) + ((byArray[n + 1] & 0xFF) << 8) + ((byArray[n + 2] & 0xFF) << 16) + ((byArray[n + 3] & 0xFF) << 24);
                    n += 4;
                    this.c[n10] = (short)(byArray[n++] & 0xFF);
                    sArray = this.d;
                    n18 = n10;
                    n17 = byArray[n++] & 0xFF;
                } else {
                    this.k[n10] = 0;
                    this.a[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                    this.b[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                    this.c[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                    sArray = this.d;
                    n18 = n10;
                    n17 = (byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8);
                }
                sArray[n18] = (short)n17;
            }
        }
        if ((n8 = (byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8)) > 0) {
            this.c = new byte[n8];
            this.f = new short[n8];
            this.g = new short[n8];
            this.d = new byte[n8];
            for (n10 = 0; n10 < n8; ++n10) {
                this.c[n10] = byArray[n++];
                this.f[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                this.g[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                this.d[n10] = byArray[n++];
            }
        }
        if ((this.f & 0x8000) != 0 && (n10 = (byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8)) > 0) {
            this.a = new byte[n10][4];
            for (n9 = 0; n9 < n10; ++n9) {
                for (n7 = 0; n7 < 4; ++n7) {
                    this.a[n9][n7] = (byte)(byArray[n++] & 0xFF);
                }
            }
        }
        int n19 = 0;
        if ((n6 = (byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8)) > 0) {
            this.b = new byte[n6];
            this.e = new short[n6];
            if ((this.f & 0x8000) != 0) {
                this.k = new short[n6];
                this.i = new byte[n6];
            }
            for (n10 = 0; n10 < n6; ++n10) {
                this.b[n10] = byArray[n++];
                this.e[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                if ((this.f & 0x8000) == 0) continue;
                this.i[n10] = (byte)(byArray[n++] & 0xFF);
                if (this.i[n10] <= 0) continue;
                this.k[n10] = (short)n19;
                n19 += this.i[n10];
            }
        }
        if ((n5 = (byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8)) > 0) {
            this.f = new byte[n5];
            this.g = new byte[n5];
            this.i = new short[n5];
            this.j = new short[n5];
            this.h = new byte[n5];
            for (n10 = 0; n10 < n5; ++n10) {
                this.f[n10] = byArray[n++];
                this.g[n10] = byArray[n++];
                this.i[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                this.j[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
                this.h[n10] = byArray[n++];
            }
        }
        if ((n4 = (byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8)) > 0) {
            this.e = new byte[n4];
            this.h = new short[n4];
            for (n10 = 0; n10 < n4; ++n10) {
                this.e[n10] = byArray[n++];
                this.h[n10] = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
            }
        }
        n10 = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
        this.g = byArray[n++] & 0xFF;
        this.h = byArray[n++] & 0xFF;
        if (this.d == null) {
            this.d = new int[this.g];
            for (n9 = 0; n9 < this.g; ++n9) {
                this.d[n9] = 1;
            }
        }
        if (this.h == 0) {
            this.h = 256;
        }
        this.a = new int[8][];
        for (n9 = 0; n9 < this.g; ++n9) {
            this.a[n9] = new int[this.h];
            if (n10 == -30584) {
                for (n7 = 0; n7 < this.h; ++n7) {
                    n3 = byArray[n++] & 0xFF;
                    n3 += (byArray[n++] & 0xFF) << 8;
                    n3 += (byArray[n++] & 0xFF) << 16;
                    if (((n3 += (byArray[n++] & 0xFF) << 24) & 0xFF000000) != -16777216) {
                        this.a = true;
                    }
                    this.a[n9][n7] = n3;
                }
                continue;
            }
            if (n10 == 17476) {
                for (n7 = 0; n7 < this.h; ++n7) {
                    n3 = byArray[n++] & 0xFF;
                    if (((n3 += (byArray[n++] & 0xFF) << 8) & 0xF000) != 61440) {
                        this.a = true;
                    }
                    this.a[n9][n7] = (n3 & 0xF000) << 16 | (n3 & 0xF000) << 12 | (n3 & 0xF00) << 12 | (n3 & 0xF00) << 8 | (n3 & 0xF0) << 8 | (n3 & 0xF0) << 4 | (n3 & 0xF) << 4 | n3 & 0xF;
                }
                continue;
            }
            if (n10 != 25861) continue;
            for (n7 = 0; n7 < this.h; ++n7) {
                int n20;
                n3 = byArray[n++] & 0xFF;
                int n21 = n++;
                n2 = -16777216;
                if ((n3 += (byArray[n21] & 0xFF) << 8) == 63519) {
                    n2 = 0;
                    this.a = true;
                }
                this.a[n9][n7] = n20 = n2 | (n3 & 0xF800) << 8 | (n3 & 0x7E0) << 5 | (n3 & 0x1F) << 3;
            }
        }
        this.a = (short)((byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8));
        if (this.a == 25840) {
            n9 = this.h - 1;
            this.j = 1;
            a a2 = this;
            int n22 = a2.k = 0;
            while (n9 != 0) {
                n9 >>= 1;
                this.j <<= 1;
                a a3 = this;
                a2 = a3;
                n22 = a3.k + 1;
            }
            --this.j;
        }
        if (this.c > 0) {
            this.c = new int[this.c];
            n9 = 0;
            n7 = n;
            for (n3 = 0; n3 < this.c; ++n3) {
                n2 = (byArray[n7++] & 0xFF) + ((byArray[n7++] & 0xFF) << 8);
                this.c[n3] = n9;
                n7 += n2;
                n9 += n2;
            }
            this.j = new byte[n9];
            for (n3 = 0; n3 < this.c; ++n3) {
                n2 = (byArray[n++] & 0xFF) + ((byArray[n++] & 0xFF) << 8);
                System.arraycopy((Object)byArray, (int)n, (Object)this.j, (int)this.c[n3], (int)n2);
                n += n2;
            }
        }
        if (this.a == null) {
            this.a = new short[10][];
            this.e = -1;
        }
    }

    public final void a(int n, int n2, int n3, int n4, int n5, int n6) {
        Object object;
        int n7;
        Object object2;
        this.d[n] = n6;
        if (this.c == 0 || (n6 & 1) != 0) {
            return;
        }
        if (n3 == -1) {
            n3 = this.c - 1;
        }
        if ((n6 & 2) != 0) {
            if (this.a == null) {
                this.a = new Image[this.g][];
            }
            if (this.a[n] == null) {
                object2 = this.a;
                n7 = n;
                object = new Image[this.c];
            }
        } else if ((n6 & 4) != 0) {
            if (this.a == null) {
                this.a = new int[this.g][][];
            }
            if (this.a[n] == null) {
                object2 = this.a;
                n7 = n;
                object = object2[n7] = (Object)new int[this.c][];
            }
        }
        if (n4 >= 0) {
            if ((n6 & 2) != 0) {
                for (int i = n2; i <= n3; ++i) {
                    this.a[n][i] = this.a[n4][i];
                }
            } else if ((n6 & 4) != 0) {
                for (int i = n2; i <= n3; ++i) {
                    this.a[n][i] = this.a[n4][i];
                }
            }
        } else {
            int n8 = this.i;
            this.i = n;
            if (n5 >= 0) {
                int n9 = 0;
                for (int i = 0; i < this.c.length; ++i) {
                    n9 = this.c[i] & 0xFF | (this.d[i] & 0xFF & 0xC0) << 2;
                    if (this.a[n5] != null) {
                        n9 = this.a[n5][n9];
                    }
                    if (((n6 & 2) == 0 || this.a[n][n9] != null) && ((n6 & 4) == 0 || this.a[n][n9] != null)) continue;
                    this.a(n9, n, n6);
                }
            } else {
                for (int i = n2; i <= n3; ++i) {
                    this.a(i, n, n6);
                }
            }
            this.i = n8;
        }
    }

    public final void a(int n, int n2, int n3) {
        int n4 = this.c[n] & 0xFF;
        int n5 = this.d[n] & 0xFF;
        if (n4 <= 0 || n5 <= 0) {
            return;
        }
        int n6 = this.i;
        this.i = n2;
        int[] nArray = this.a(n);
        this.i = n6;
        if (nArray == null) {
            return;
        }
        int n7 = n4 * n5;
        boolean bl = false;
        for (int i = 0; i < n7; ++i) {
            if ((nArray[i] & 0xFF000000) == -16777216) continue;
            bl = true;
            break;
        }
        if ((n3 & 2) != 0) {
            this.a[n2][n] = Image.createRGBImage((int[])nArray, (int)n4, (int)n5, (boolean)bl);
            return;
        }
        if ((n3 & 4) != 0) {
            this.a[n2][n] = new int[n7];
            System.arraycopy((Object)nArray, (int)0, (Object)this.a[n2][n], (int)0, (int)n7);
        }
    }

    public final void a() {
        this.j = null;
        this.c = null;
    }

    public final void b() {
        this.a = null;
        this.b = null;
        this.c = null;
        this.d = null;
        this.b = null;
        this.e = null;
        this.c = null;
        this.f = null;
        this.g = null;
        this.d = null;
        this.e = null;
        this.h = null;
        this.f = null;
        this.g = null;
        this.i = null;
        this.j = null;
        this.h = null;
        this.a = null;
        this.j = null;
        this.c = null;
        this.a = null;
        if (this.a != null) {
            for (int i = 0; i < this.a.length; ++i) {
                if (this.a[i] == null) continue;
                for (int j = 0; j < this.a[i].length; ++j) {
                    this.a[i][j] = null;
                }
            }
        }
    }

    public final void a(int n, byte[] byArray) {
        int n2;
        this.d |= 1 << n;
        if (byArray == null) {
            return;
        }
        if (this.a[n] == null) {
            this.a[n] = new short[this.c];
            n2 = 0;
            short s = (short)n2;
            while (s < this.c) {
                this.a[n][n2] = n2;
                s = (short)(n2 + 1);
            }
        }
        int n3 = 0;
        while (n3 < byArray.length) {
            n2 = (byArray[n3++] & 0xFF) + ((byArray[n3++] & 0xFF) << 8);
            int n4 = (byArray[n3++] & 0xFF) + ((byArray[n3++] & 0xFF) << 8);
            this.a[n][n2] = (short)n4;
        }
    }

    public final int a(int n, int n2) {
        return this.g[this.h[n] + n2] & 0xFF;
    }

    public final int a(int n) {
        return this.e[n] & 0xFF;
    }

    public final int b(int n) {
        return this.b[n] & 0xFF;
    }

    public final int b(int n, int n2) {
        int n3 = this.h[n] + n2;
        int n4 = this.f[n3] & 0xFF;
        return n4 |= (this.h[n3] & 0xC0) << 2;
    }

    public final void a(int[] nArray, int n, int n2, int n3, int n4, int n5) {
        m = 102400;
        a.n = 102400;
        o = -102400;
        p = -102400;
        l = 1;
        this.a(n, n2, n3, n4, n5);
        l = 0;
        nArray[0] = m;
        nArray[1] = a.n;
        nArray[2] = o;
        nArray[3] = p;
    }

    public final void a(int[] nArray, int n, int n2, int n3, int n4) {
        m = 0x1900000;
        a.n = 0x1900000;
        o = -26214400;
        p = -26214400;
        l = 1;
        this.a(n, n2, n3, n4);
        l = 0;
        nArray[0] = m;
        nArray[1] = a.n;
        nArray[2] = o;
        nArray[3] = p;
    }

    public final void b(int[] nArray, int n, int n2, int n3, int n4, int n5) {
        m = 102400;
        a.n = 102400;
        o = -102400;
        p = -102400;
        l = 1;
        this.b(n, n2, n3, n4, n5);
        l = 0;
        nArray[0] = m;
        nArray[1] = a.n;
        nArray[2] = o;
        nArray[3] = p;
    }

    public final void b(int[] nArray, int n, int n2, int n3, int n4) {
        m = 102400;
        a.n = 102400;
        o = -102400;
        p = -102400;
        l = 1;
        this.b(n, n2, n3, n4);
        l = 0;
        nArray[0] = m;
        nArray[1] = a.n;
        nArray[2] = o;
        nArray[3] = p;
    }

    public static void a(Graphics graphics) {
        a = graphics;
    }

    public static Graphics a() {
        return a;
    }

    public final void a(Graphics graphics, int n, int n2, int n3, int n4, int n5) {
        a.a(graphics);
        this.a(n, n2, n3, n4, n5);
    }

    public final void a(Graphics graphics, int n, int n2, int n3, int n4) {
        a.a(graphics);
        this.a(n, n2, n3, n4);
    }

    public final void c(int[] nArray, int n, int n2, int n3, int n4, int n5) {
        this.a(nArray, n, n2, n3, n4, n5);
    }

    public final void c(int[] nArray, int n, int n2, int n3, int n4) {
        this.a(nArray, n, n2, n3, n4);
    }

    public final byte[] a(int n, int n2) {
        return this.a[this.k[n] + n2];
    }

    /*
     * Unable to fully structure code
     */
    public final void a(int var1_1, int var2_2, int var3_3, int var4_4, int var5_5) {
        block5: {
            block3: {
                block4: {
                    var6_6 = this.h[var1_1] + var2_2;
                    var7_7 = this.f[var6_6] & 255;
                    var7_7 |= (this.h[var6_6] & 192) << 2;
                    if (((var5_5 ^ this.h[var6_6] & 15) & 4) == 0) break block3;
                    v0 = var3_3 = (var5_5 & 1) != 0 ? var3_3 + this.i[var6_6] : var3_3 - this.i[var6_6];
                    if ((var5_5 & 2) == 0) break block4;
                    v1 = var4_4 - this.j[var6_6];
                    break block5;
                }
                v2 = var4_4;
                ** GOTO lbl18
            }
            v3 = var3_3 = (var5_5 & 1) != 0 ? var3_3 - this.i[var6_6] : var3_3 + this.i[var6_6];
            if ((var5_5 & 2) != 0) {
                v1 = var4_4 - this.j[var6_6];
            } else {
                v2 = var4_4;
lbl18:
                // 2 sources

                v1 = var4_4 = v2 + this.j[var6_6];
            }
        }
        if ((g.ag & 32) != 0) {
            g.a(this, var7_7, var3_3, var4_4, var5_5 ^ this.h[var6_6] & 15);
            return;
        }
        this.a(var7_7, var3_3, var4_4, var5_5 ^ this.h[var6_6] & 15);
    }

    public final void a(int n, int n2, int n3, int n4) {
        int n5 = this.b[n] & 0xFF;
        for (int i = 0; i < n5; ++i) {
            this.b(n, i, n2, n3, n4);
        }
    }

    public final void b(int n, int n2, int n3, int n4, int n5) {
        int n6;
        int n7;
        block19: {
            int n8;
            int n9;
            block20: {
                int n10;
                int n11;
                block18: {
                    block16: {
                        short[] sArray;
                        int n12;
                        block14: {
                            block17: {
                                block12: {
                                    block15: {
                                        block13: {
                                            int n13 = this.e[n] + n2;
                                            n7 = this.d[n13] & 0xFF;
                                            n6 = this.c[n13] & 0xFF;
                                            n6 |= (n7 & 0xC0) << 2;
                                            int n14 = this.f[n13];
                                            int n15 = this.g[n13];
                                            if ((this.d[this.i] & 4) != 0 && (g.ag & 1) != 0) {
                                                int n16 = g.b() - 100;
                                                n14 += n16 * n14 / 100 >> 1;
                                                n15 += n16 * n15 / 100 >> 1;
                                            }
                                            if ((n5 & 4) != 0) {
                                                int n17 = n4 = (n5 & 1) != 0 ? n4 - this.f[n13] : n4 + n14;
                                                n3 = (n5 & 2) != 0 ? (n3 -= this.g[n13]) : (n3 += n15);
                                            } else {
                                                n3 = (n5 & 1) != 0 ? n3 - this.f[n13] : n3 + n14;
                                                n4 = (n5 & 2) != 0 ? n4 - this.g[n13] : n4 + n15;
                                            }
                                            n11 = 0;
                                            n10 = 0;
                                            if ((n7 & 4) == 0) break block12;
                                            if ((n5 & 2) == 0 || (n5 & 1) != 0) break block13;
                                            n5 |= 1;
                                            n5 &= 0xFFFFFFFD;
                                            n12 = 0;
                                            sArray = this.c;
                                            break block14;
                                        }
                                        if ((n5 & 1) == 0 || (n5 & 2) != 0) break block15;
                                        n5 |= 2;
                                        n5 &= 0xFFFFFFFE;
                                        n11 = 0 - (this.d[n6] & 0xFF);
                                        break block16;
                                    }
                                    if ((n5 & 1) != 0) {
                                        n11 = 0 - (this.c[n6] & 0xFF);
                                    }
                                    if ((n5 & 2) == 0) break block16;
                                    break block17;
                                }
                                if ((n5 & 1) != 0) {
                                    n11 = 0 - (this.c[n6] & 0xFF);
                                }
                                if ((n5 & 2) == 0) break block16;
                            }
                            n12 = 0;
                            sArray = this.d;
                        }
                        n10 = n12 - (sArray[n6] & 0xFF);
                    }
                    if ((n5 & 4) == 0) break block18;
                    if ((n7 & 0x10) != 0) break block19;
                    n3 += n10;
                    n9 = n4;
                    n8 = n11;
                    break block20;
                }
                if ((n7 & 0x10) != 0) break block19;
                n3 += n11;
                n9 = n4;
                n8 = n10;
            }
            n4 = n9 + n8;
        }
        if ((n7 & 0x10) != 0) {
            this.a(n6, n3, n4, n5 ^ n7 & 0xF);
            return;
        }
        this.b(n6, n3, n4, n5 ^ n7 & 0xF);
    }

    public final void b(int n, int n2, int n3, int n4) {
        int n5;
        int n6;
        block43: {
            block45: {
                int n7;
                int n8;
                block46: {
                    block44: {
                        if (this.e >= 0 && this.a[this.e] != null) {
                            n = this.a[this.e][n];
                        }
                        n6 = this.c[n] & 0xFF;
                        n5 = this.d[n] & 0xFF;
                        if (n6 <= 0 || n5 <= 0) {
                            return;
                        }
                        if (l != 1) break block43;
                        if (n2 < m) {
                            m = n2;
                        }
                        if (n3 < a.n) {
                            a.n = n3;
                        }
                        if ((n4 & 4) != 0) break block44;
                        if (n2 + n6 > o) {
                            o = n2 + n6;
                        }
                        if (n3 + n5 <= p) break block45;
                        n8 = n3;
                        n7 = n5;
                        break block46;
                    }
                    if (n2 + n5 > o) {
                        o = n2 + n5;
                    }
                    if (n3 + n6 <= p) break block45;
                    n8 = n3;
                    n7 = n6;
                }
                p = n8 + n7;
            }
            return;
        }
        int n9 = a.getClipX();
        int n10 = a.getClipY();
        int n11 = a.getClipWidth();
        int n12 = a.getClipHeight();
        if ((n4 & 4) == 0 ? n2 + n6 < n9 || n3 + n5 < n10 || n2 >= n9 + n11 || n3 >= n10 + n12 : n2 + n5 < n9 || n3 + n6 < n10 || n2 >= n9 + n11 || n3 >= n10 + n12) {
            return;
        }
        if (this.k[n] != 0) {
            if ((n4 & 4) != 0) {
                int n13 = n6;
                n6 = n5;
                n5 = n13;
            }
            a.setColor(this.e[n]);
            if (this.k[n] != 1) {
                if ((g.ag & 0x40) != 0) {
                    g.b(a, this.e[n], n2, n3, n6, n5);
                } else if ((this.e[n] & 0xFF000000) != 0 && (this.e[n] & 0xFF000000) != -16777216) {
                    g.b(a, this.e[n], n2, n3, n6, n5);
                } else {
                    a.fillRect(n2, n3, n6, n5);
                }
            }
            if ((g.ag & 4) != 0) {
                g.a(a, this.e[n], n2, n3, n6, n5);
            }
            return;
        }
        Image image = null;
        int[] nArray = null;
        if ((this.d[this.i] & 2) != 0) {
            if (this.a != null && this.a[this.i] != null) {
                image = this.a[this.i][n];
            }
        } else if ((this.d[this.i] & 4) != 0) {
            nArray = this.a[this.i][n];
            int n14 = g.ag;
            if ((n14 & 1) != 0) {
                nArray = g.a(nArray, n6, n5);
                int n15 = g.b();
                n6 = n6 * n15 / 100;
                n5 = n5 * n15 / 100;
            }
            if ((n14 & 2) != 0) {
                nArray = g.b(nArray, n6, n5);
                this.a = true;
            }
        }
        if (image == null && nArray == null) {
            int[] nArray2 = this.a(n);
            if (nArray2 == null) {
                return;
            }
            image = Image.createRGBImage((int[])nArray2, (int)n6, (int)n5, (boolean)this.a);
        }
        if (l == 0) {
            if (image != null) {
                if ((g.ag & 0x80) != 0) {
                    g.a(a, image, n2, n3);
                } else if ((n4 & 7) == 0) {
                    a.drawImage(image, n2, n3, 0);
                } else {
                    a.drawRegion(image, 0, 0, n6, n5, a[n4 & 7], n2, n3, 0);
                }
            } else if (nArray != null) {
                if ((g.ag & 0x80) != 0) {
                    g.a(a, nArray, n6, n5, n2, n3);
                } else if ((g.ag & 0x18) != 0) {
                    try {
                        g.a(a, n2, n3, nArray, n6, n5, n4);
                    }
                    catch (Exception exception) {}
                } else {
                    nArray = g.a(a, nArray, n2, n3, n6, n5, n4, this.a);
                }
            }
        }
        if ((this.d[this.i] & 4) != 0 && (g.ag & 4) != 0) {
            if ((n4 & 4) != 0) {
                int n16 = n6;
                n6 = n5;
                n5 = n16;
            }
            g.a(a, n2, n3, nArray, n6, n5);
        }
    }

    private int[] a(int n) {
        int[] nArray;
        block17: {
            int[] nArray2;
            int n2;
            int n3;
            int n4;
            byte[] byArray;
            block24: {
                block23: {
                    block22: {
                        block21: {
                            block20: {
                                block19: {
                                    block18: {
                                        if (this.j == null || this.c == null || this.k[n] != 0) {
                                            return null;
                                        }
                                        int n5 = this.c[n] & 0xFF;
                                        int n6 = this.d[n] & 0xFF;
                                        byArray = this.j;
                                        n4 = this.c[n];
                                        n3 = 0;
                                        n2 = n5 * n6;
                                        nArray = b;
                                        nArray2 = this.a[this.i];
                                        if (nArray2 == null) {
                                            return null;
                                        }
                                        if (this.a != 25840) break block18;
                                        while (n3 < n2) {
                                            int n7 = byArray[n4++] & 0xFF;
                                            int n8 = nArray2[n7 & this.j];
                                            n7 >>= this.k;
                                            while (n7-- >= 0) {
                                                nArray[n3++] = n8;
                                            }
                                        }
                                        break block17;
                                    }
                                    if (this.a != 10225) break block19;
                                    while (n3 < n2) {
                                        int n9;
                                        if ((n9 = byArray[n4++] & 0xFF) > 127) {
                                            int n10 = byArray[n4++] & 0xFF;
                                            int n11 = nArray2[n10];
                                            n9 -= 128;
                                            while (n9-- > 0) {
                                                nArray[n3++] = n11;
                                            }
                                            continue;
                                        }
                                        nArray[n3++] = nArray2[n9];
                                    }
                                    break block17;
                                }
                                if (this.a != 22258) break block20;
                                while (n3 < n2) {
                                    int n12;
                                    if ((n12 = byArray[n4++] & 0xFF) > 127) {
                                        n12 -= 128;
                                        while (n12-- > 0) {
                                            nArray[n3++] = nArray2[byArray[n4++] & 0xFF];
                                        }
                                        continue;
                                    }
                                    int n13 = nArray2[byArray[n4++] & 0xFF];
                                    while (n12-- > 0) {
                                        nArray[n3++] = n13;
                                    }
                                }
                                break block17;
                            }
                            if (this.a != 5632) break block21;
                            while (n3 < n2) {
                                nArray[n3++] = nArray2[byArray[n4] >> 4 & 0xF];
                                nArray[n3++] = nArray2[byArray[n4] & 0xF];
                                ++n4;
                            }
                            break block17;
                        }
                        if (this.a != 2048) break block22;
                        while (n3 < n2) {
                            nArray[n3++] = nArray2[byArray[n4] >> 5 & 7];
                            nArray[n3++] = nArray2[byArray[n4] >> 2 & 7];
                            if (n3 >= n2) break block17;
                            nArray[n3++] = nArray2[byArray[n4] << 1 & 6 | byArray[++n4] >> 7 & 1];
                            nArray[n3++] = nArray2[byArray[n4] >> 4 & 7];
                            nArray[n3++] = nArray2[byArray[n4] >> 1 & 7];
                            if (n3 < n2) {
                                nArray[n3++] = nArray2[byArray[n4] << 2 & 4 | byArray[++n4] >> 6 & 3];
                                nArray[n3++] = nArray2[byArray[n4] >> 3 & 7];
                                nArray[n3++] = nArray2[byArray[n4] & 7];
                                ++n4;
                                continue;
                            }
                            break block17;
                        }
                        break block17;
                    }
                    if (this.a != 1024) break block23;
                    while (n3 < n2) {
                        nArray[n3++] = nArray2[byArray[n4] >> 6 & 3];
                        nArray[n3++] = nArray2[byArray[n4] >> 4 & 3];
                        nArray[n3++] = nArray2[byArray[n4] >> 2 & 3];
                        nArray[n3++] = nArray2[byArray[n4] & 3];
                        ++n4;
                    }
                    break block17;
                }
                if (this.a != 512) break block24;
                while (n3 < n2) {
                    nArray[n3++] = nArray2[byArray[n4] >> 7 & 1];
                    nArray[n3++] = nArray2[byArray[n4] >> 6 & 1];
                    nArray[n3++] = nArray2[byArray[n4] >> 5 & 1];
                    nArray[n3++] = nArray2[byArray[n4] >> 4 & 1];
                    nArray[n3++] = nArray2[byArray[n4] >> 3 & 1];
                    nArray[n3++] = nArray2[byArray[n4] >> 2 & 1];
                    nArray[n3++] = nArray2[byArray[n4] >> 1 & 1];
                    nArray[n3++] = nArray2[byArray[n4] & 1];
                    ++n4;
                }
                break block17;
            }
            if (this.a != 22018) break block17;
            while (n3 < n2) {
                nArray[n3++] = nArray2[byArray[n4++] & 0xFF];
            }
        }
        return nArray;
    }

    public final int a() {
        return this.d[0] & 0xFF;
    }

    public final void a(int n) {
        if (n < this.g) {
            this.i = n;
        }
    }

    static {
        a = new int[]{0, 2, 1, 3, 5, 7, 4, 6};
        b = new int[16384];
        l = 0;
    }
}
