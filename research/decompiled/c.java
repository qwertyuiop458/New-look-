/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  java.lang.Object
 *  javax.microedition.lcdui.Graphics
 */
import javax.microedition.lcdui.Graphics;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public final class c {
    public int a;
    public int b;
    public int c;
    public a a;
    public int d;
    public int e;
    public int f;
    public int[] a;
    public int g;
    public boolean a;
    public int h;
    public int i;
    public c a;
    public static int j;
    public static int k;

    public c() {
    }

    public c(a a2, int n, int n2, c c2) {
        this.a = n << 14;
        this.b = n2 << 14;
        this.a = a2;
        this.a = new int[4];
        this.a = c2;
        this.a = false;
    }

    public static void a(int n) {
        j += n;
        int n2 = k = 0;
        while (j >= 62) {
            j -= 62;
            n2 = k + 1;
        }
    }

    public final void b(int n) {
        this.d = n;
        this.e = 0;
        this.f = 0;
        this.g = -1;
        this.a = false;
        this.h = 1;
        this.i = -1;
        if (this.a != null) {
            this.i = this.a.a(this.d) - 1;
        }
    }

    public final void a(int n, int n2) {
        this.b(n);
        this.g = n2;
    }

    public final void a(int n, int n2, int n3) {
        this.b(n);
        this.g = n3;
        this.h = n2;
        if (this.h == 1) {
            this.i = this.a.a(this.d) - 1;
            return;
        }
        this.i = 0;
        this.e = this.a.a(this.d) - 1;
    }

    public final void a(a a2) {
        this.a = a2;
        if (this.f >= 0 && this.i < 0) {
            if (this.h == 1) {
                this.i = this.a.a(this.d) - 1;
                return;
            }
            this.i = 0;
            this.e = this.a.a(this.d) - 1;
        }
    }

    public final boolean a() {
        if (this.a) {
            this.e = this.a.a(this.d) - 1;
        }
        return this.a;
    }

    public final void a(Graphics graphics) {
        c c2;
        if (this.a == null) {
            return;
        }
        int n = this.a;
        int n2 = this.b;
        c c3 = this;
        while ((c2 = c3.a) != null) {
            n += c2.a;
            n2 += c2.b;
            c3 = c2;
        }
        n = c.a(n) + 0;
        n2 = c.b(n2) + 0;
        a.a(graphics);
        if (this.f >= 0) {
            this.a.a(this.d, this.e, n, n2, this.c);
            return;
        }
        if (this.d >= 0) {
            this.a.b(this.d, n, n2, this.c);
            return;
        }
        if (this.e >= 0) {
            this.a.a(this.e, n, n2, this.c);
        }
    }

    public final void a() {
        this.a = false;
        if (this.a == null) {
            return;
        }
        if (this.f < 0) {
            return;
        }
        for (int i = 0; i < k; ++i) {
            boolean bl;
            block12: {
                block13: {
                    c c2;
                    block11: {
                        int n = this.a.a(this.d, this.e);
                        if (n == 0) {
                            return;
                        }
                        ++this.f;
                        if (n > this.f) continue;
                        this.f = 0;
                        this.e += this.h;
                        bl = false;
                        if (this.h != 1) break block11;
                        if (this.e <= this.i) break block12;
                        if (this.g == -1 || this.g > 0) {
                            this.e = 0;
                            bl = true;
                        } else {
                            this.e = this.a.a(this.d) - 1;
                        }
                        c2 = this;
                        break block13;
                    }
                    if (this.e >= this.i) break block12;
                    if (this.g == -1 || this.g > 0) {
                        this.e = this.a.a(this.d) - 1;
                        bl = true;
                    } else {
                        this.e = 0;
                    }
                    c2 = this;
                }
                c2.a = true;
            }
            if (!bl || this.g == -1) continue;
            --this.g;
        }
    }

    public final int[] a() {
        int n = this.a;
        int n2 = this.b;
        n = c.a(n) + 0;
        n2 = c.b(n2) + 0;
        if (this.a == null) {
            this.a = new int[4];
        }
        if (this.a != null) {
            if (this.f >= 0) {
                this.a.c(this.a, this.d, this.e, n, n2, this.c);
            } else if (this.d >= 0) {
                this.a.b(this.a, this.d, n, n2, this.c);
            } else if (this.e >= 0) {
                this.a.c(this.a, this.e, n, n2, this.c);
            }
        }
        return this.a;
    }

    public static int a(int n) {
        return (n >> 14) * 1 / 1;
    }

    public static int b(int n) {
        return (n >> 14) * 1 / 1;
    }

    public final void c(int n) {
        this.a = n << 14;
    }

    public final void d(int n) {
        this.b = n << 14;
    }

    public final void b(int n, int n2) {
        this.a = n << 14;
        this.b = n2 << 14;
    }

    public final int a() {
        return this.a >> 14;
    }

    public final int b() {
        return this.b >> 14;
    }
}
