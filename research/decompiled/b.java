/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  java.io.InputStream
 *  java.lang.Exception
 *  java.lang.Integer
 *  java.lang.Math
 *  java.lang.Object
 *  java.lang.Runnable
 *  java.lang.RuntimeException
 *  java.lang.String
 *  java.lang.StringBuffer
 *  java.lang.System
 *  java.lang.Thread
 *  java.util.Hashtable
 *  javax.microedition.lcdui.Canvas
 *  javax.microedition.lcdui.Command
 *  javax.microedition.lcdui.CommandListener
 *  javax.microedition.lcdui.Displayable
 *  javax.microedition.lcdui.Font
 *  javax.microedition.lcdui.Graphics
 *  javax.microedition.lcdui.Image
 *  javax.microedition.midlet.MIDlet
 *  javax.microedition.rms.RecordStore
 */
import java.io.InputStream;
import java.util.Hashtable;
import javax.microedition.lcdui.Canvas;
import javax.microedition.lcdui.Command;
import javax.microedition.lcdui.CommandListener;
import javax.microedition.lcdui.Displayable;
import javax.microedition.lcdui.Font;
import javax.microedition.lcdui.Graphics;
import javax.microedition.lcdui.Image;
import javax.microedition.midlet.MIDlet;
import javax.microedition.rms.RecordStore;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public final class b
implements Runnable,
CommandListener {
    public static String a = "1.9";
    public static String b = "IGP-Signature=" + a;
    private static String c = "";
    private static String d;
    private static boolean c;
    private static Font a;
    private static int a;
    private static int b;
    private static int c;
    private static int d;
    private static int e;
    private static int f;
    private static int g;
    private static int h;
    private static int i;
    private static int j;
    private static int k;
    private static int l;
    private static int m;
    private static int n;
    private static int o;
    private static int p;
    private static int q;
    private static int r;
    private static int s;
    private static int t;
    private static int u;
    private static int v;
    private static int w;
    private static int x;
    private static int[] a;
    private static byte[][] a;
    private static int y;
    private static byte[] a;
    private static int z;
    private static int A;
    private static int B;
    private static int C;
    private static int D;
    private static Image[] a;
    private static int E;
    private static int[] b;
    private static int F;
    private static int G;
    private static boolean d;
    private static final String[] b;
    private static String e;
    private static boolean e;
    public static String[] a;
    private static String[] c;
    private static String[] d;
    private static String[] e;
    private static int H;
    private static int I;
    private static String[] f;
    private static short[] a;
    private static int J;
    private static int K;
    private static int L;
    private static boolean f;
    private static boolean g;
    private static boolean h;
    private static boolean i;
    private static long a;
    private static boolean j;
    private static MIDlet a;
    private static Canvas a;
    private static String f;
    private static boolean k;
    private static CommandListener a;
    public static b a;
    private static boolean l;
    private static String g;
    private static boolean m;
    private static int M;
    private static int N;
    private static int O;
    private static int P;
    private static int Q;
    private static int R;
    private static Image[] b;
    private static Image[] c;
    private static Image a;
    private static Image b;
    private static Image c;
    private static Image[][] a;
    private static String[][] a;
    private static int[][] a;
    private static int[][] b;
    private static int[] c;
    private static int S;
    private static int T;
    private static int U;
    private static int V;
    private static int W;
    private static int X;
    private static int Y;
    private static int Z;
    private static int aa;
    private static int ab;
    private static int ac;
    private static String[] g;
    private static boolean[] a;
    private static int ad;
    private static boolean n;
    private static byte a;
    private static boolean o;
    private static int ae;
    private static int af;
    private static int ag;
    private static int ah;
    private static int ai;
    private static int aj;
    private static Image d;
    private static Image e;
    private static String h;
    private static String i;
    private static String j;
    private static int ak;
    private static int al;
    private static int am;
    private static int an;
    private static Command a;
    private static Command b;
    private static int ao;
    private static boolean p;
    private static boolean q;
    private static String k;
    private static Hashtable a;
    private static String l;
    private static String m;
    private static String n;
    private static String o;
    private static String p;
    private static String q;
    private static String r;
    private static String s;
    private static String t;
    private static String u;
    private static int ap;
    public static boolean a;
    public static boolean b;

    private static boolean b() {
        b.a();
        try {
            InputStream inputStream = "a".getClass().getResourceAsStream("/dataIGP");
            x = inputStream.read() & 0xFF;
            a = new int[x += (inputStream.read() & 0xFF) << 8];
            int n = 0;
            while (n < x) {
                b.a[n] = inputStream.read() & 0xFF;
                int n2 = n;
                a[n2] = a[n2] + ((inputStream.read() & 0xFF) << 8);
                int n3 = n;
                a[n3] = a[n3] + ((inputStream.read() & 0xFF) << 16);
                int n4 = n++;
                a[n4] = a[n4] + ((inputStream.read() & 0xFF) << 24);
            }
            inputStream.close();
        }
        catch (Exception exception) {
            return false;
        }
        return true;
    }

    private static void a() {
        a = null;
        a = null;
        x = 0;
        System.gc();
    }

    private static byte[] a(int n) {
        if (n < 0 || n >= x - 1) {
            return null;
        }
        int n2 = a[n + 1] - a[n];
        if (n2 == 0) {
            return null;
        }
        if (a != null) {
            return a[n];
        }
        byte[] byArray = null;
        try {
            int n3;
            InputStream inputStream = null;
            inputStream = "a".getClass().getResourceAsStream("/dataIGP");
            inputStream.skip((long)(2 + 4 * x + a[n]));
            byArray = new byte[n2];
            int n4 = n3 = byArray.length;
            while (n4 > 0) {
                n4 = n3 - inputStream.read(byArray);
            }
            inputStream.close();
        }
        catch (Exception exception) {}
        return byArray;
    }

    private static int a(byte[] byArray) {
        return (byArray[y++] & 0xFF) + ((byArray[y++] & 0xFF) << 8);
    }

    private static Image a(byte[] byArray) {
        int n = b.a(byArray);
        Image image = b.a(byArray, y, n);
        y += n;
        return image;
    }

    private static Image a(byte[] byArray, int n, int n2) {
        if (d.d) {
            byte[] byArray2 = new byte[n2];
            System.arraycopy((Object)byArray, (int)n, (Object)byArray2, (int)0, (int)n2);
            byArray = byArray2;
            n = 0;
        }
        return Image.createImage((byte[])byArray, (int)n, (int)n2);
    }

    private static String a(int n) {
        return "" + f[n];
    }

    private static int a(int n, int n2) {
        if (ap != 0) {
            if (n2 == A || n2 == B) {
                int n3 = a[n * 6 + n2] & 0xFF;
                int n4 = a[n * 6 + n2 + 1] & 0xFF;
                int n5 = 0;
                n5 = 0 | (n4 & 0xFF) << 8;
                return n5 |= n3 & 0xFF;
            }
            int n6 = a[n * 6 + n2] & 0xFF;
            return n6;
        }
        return a[(n << 2) + n2] & 0xFF;
    }

    private static void a(int n, Graphics graphics, int n2, int n3, int n4) {
        b.a(b.a(n), graphics, ak, n2, n3, n4);
    }

    private static void a(String string, Graphics graphics, int n, int n2, int n3, int n4) {
        b.a(string, graphics, n2, n3, n4);
    }

    /*
     * Unable to fully structure code
     */
    private static void a(String var0, Graphics var1_1, int var2_2, int var3_3, int var4_4) {
        block17: {
            block20: {
                block19: {
                    block18: {
                        var5_5 = var0;
                        b.b[0] = 0;
                        b.G = 0;
                        var6_6 = 0;
                        var9_7 = false;
                        var10_8 = false;
                        var11_9 = var5_5.length();
                        var12_10 = 0;
                        if (b.ak <= 176 && (b.O == 0 || b.O == 1 || b.O == 2)) {
                            var12_10 += 2;
                        }
                        for (var8_11 = 0; var8_11 < var11_9; ++var8_11) {
                            var7_12 = var5_5.charAt(var8_11);
                            if (var7_12 == '\n' && var6_6 < 10 || var7_12 == '\\' && var5_5.charAt(++var8_11) == 'N') {
                                v0 = var6_6;
                                b.b[v0] = b.b[v0] - -1;
                                if (b.b[var6_6] > b.G) {
                                    b.G = b.b[var6_6];
                                }
                                v1 = b.b;
                                v2 = ++var6_6;
                                v3 = 0;
                            } else {
                                if (var7_12 == '\u0000' || var7_12 == '\u0001') continue;
                                v4 = var6_6;
                                v2 = v4;
                                v1 = b.b;
                                v3 = b.b[v4] + (b.a(var7_12, b.C) + -1);
                            }
                            v1[v2] = v3;
                        }
                        v5 = var6_6;
                        b.b[v5] = b.b[v5] - -1;
                        if (b.b[var6_6] > b.G) {
                            b.G = b.b[var6_6];
                        }
                        b.F = (var6_6 + 1) * b.z + var6_6 * (0 + var12_10);
                        if (b.d) break block17;
                        var3_3 += (0 + var12_10) * var6_6 / 2;
                        var6_6 = 0;
                        if ((var4_4 & 32) == 0) break block18;
                        v6 = var3_3;
                        v7 = b.F;
                        break block19;
                    }
                    if ((var4_4 & 2) == 0) break block20;
                    v6 = var3_3;
                    v7 = b.F >> 1;
                }
                var3_3 = v6 - v7;
            }
            var13_13 = var2_2;
            var9_7 = true;
            var10_8 = false;
            b.b(var1_1, 0, 0, b.ak, b.al);
            for (var8_11 = 0; var8_11 < var11_9; ++var8_11) {
                block21: {
                    block24: {
                        block23: {
                            block22: {
                                var7_12 = var5_5.charAt(var8_11);
                                if (!var9_7) break block21;
                                var13_13 = var2_2;
                                if ((var4_4 & 8) == 0) break block22;
                                v8 = var13_13;
                                v9 = b.b[var6_6];
                                break block23;
                            }
                            if ((var4_4 & 1) == 0) break block24;
                            v8 = var13_13;
                            v9 = b.b[var6_6] >> 1;
                        }
                        var13_13 = v8 - v9;
                    }
                    var9_7 = false;
                }
                if (var7_12 == '\n' && var6_6 < 10 || var7_12 == '\\' && var5_5.charAt(++var8_11) == 'N') {
                    var3_3 += b.z + 0 + var12_10 - 2;
                    ++var6_6;
                    var9_7 = true;
                    var10_8 = true;
                    continue;
                }
                if (!var10_8) ** GOTO lbl-1000
                var10_8 = false;
                var14_14 = var5_5.charAt(var8_11 - 2);
                if (var14_14 == ' ') {
                    var13_13 -= b.a(var14_14, b.C) + -1 >> 1;
                }
                if (var7_12 == ' ') {
                    v10 = var13_13;
                    v11 = b.a(var7_12, b.C) + -1 >> 1;
                } else lbl-1000:
                // 2 sources

                {
                    b.b(var1_1, var13_13, var3_3, b.a(var7_12, b.C), b.a(var7_12, b.D));
                    b.a(var1_1, b.a[b.E], b.a(var7_12, b.A), b.a(var7_12, b.B), b.a(var7_12, b.C), b.a(var7_12, b.D), var13_13, var3_3);
                    v10 = var13_13;
                    v11 = b.a(var7_12, b.C) + -1;
                }
                var13_13 = v10 + v11;
            }
            b.b(var1_1, 0, 0, b.ak, b.al);
            b.E = 0;
            return;
        }
        b.d = false;
    }

    public static void a(MIDlet mIDlet, Canvas canvas, int n, int n2) {
        b.a(mIDlet, canvas, n, n2, null);
    }

    private static void a(MIDlet mIDlet, Canvas canvas, int n, int n2, CommandListener commandListener) {
        ak = n;
        al = n2;
        am = ak >> 1;
        an = al >> 1;
        if (d.a < 0 || d.a > ak / 2 - ak * 15 / 100) {
            b = 2;
        }
        if (a != null) {
            return;
        }
        if (mIDlet == null) {
            System.out.println("MIDlet instance can't be null");
            return;
        }
        if (canvas == null) {
            System.out.println("Canvas instance can't be null");
            return;
        }
        if (commandListener != null) {
            k = true;
            if (a == null) {
                a = new b();
            }
            a = commandListener;
        }
        a = mIDlet;
        a = canvas;
        if (d.i) {
            b.h();
        }
        b.b();
        String string = b;
        String cfr_ignored_0 = string + "";
    }

    private static boolean a(String string, int n) {
        if (string == null) {
            return (n & 1) == 0;
        }
        string = string.trim();
        return !((n & 1) != 0 && string.length() == 0 || (n & 2) != 0 && string.toUpperCase().compareTo("DEL") == 0 || (n & 4) != 0 && (string.toUpperCase().compareTo("NO") == 0 || string.toUpperCase().compareTo("0") == 0));
    }

    private static String a(String string, String string2, String string3) {
        String string4 = "";
        try {
            if (string3 != null && string != null && string2 != null) {
                int n = string.indexOf(string2 + "=");
                string3 = string3.trim();
                if (n >= 0 && string3.length() > 0) {
                    int n2 = string.indexOf(";", n += string2.length() + 1);
                    if (n2 < 0) {
                        n2 = string.length();
                    }
                    string4 = string.substring(n, n2);
                    if ((string4 = string4.trim()).length() == 0 || string4.compareTo("0") == 0 || string4.toUpperCase().compareTo("NO") == 0) {
                        string4 = "";
                    } else if (string4.toUpperCase().compareTo("DEL") != 0 && string2.compareTo("OP") != 0) {
                        int n3 = string3.indexOf("XXXX");
                        string4 = string3.substring(0, n3) + string4 + string3.substring(n3 + "XXXX".length());
                    }
                }
            }
        }
        catch (Exception exception) {
            string4 = "";
        }
        return string4;
    }

    private static void a(int n, String string, int n2, String string2, String string3) {
        try {
            String string4 = null;
            string4 = e ? b.a(b.a(string2), string, string3) : b.a("URL-" + string);
            boolean bl = b.a(string4, n2);
            if (bl && (string4.toUpperCase().compareTo("NO") != 0 || string4.toUpperCase().compareTo("0") != 0)) {
                b.g[n] = string4;
                b.a[n] = true;
            }
            return;
        }
        catch (Exception exception) {
            return;
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void a(int var0, String[] var1_1, int var2_2, String var3_3) {
        var4_4 = var1_1.length;
        b.a[var0] = new String[var4_4];
        b.a[var0] = new int[var4_4];
        b.b[var0] = new int[var4_4];
        var5_5 = 0;
        if (b.c) {
            return;
        }
        var6_6 = "";
        if (b.e) {
            try {
                var3_3 = b.a(var3_3);
                if (var0 != 2) {
                    var6_6 = b.e;
                } else if (b.j.length() > 0) {
                    var6_6 = b.j + "&ctg=XXXX";
                }
            }
            catch (Exception v0) {}
        }
        for (var7_7 = 0; var7_7 < var1_1.length; ++var7_7) {
            try {
                block16: {
                    block14: {
                        block15: {
                            var8_8 = "";
                            if (var0 == 2 || var7_7 != var4_4 - 1) break block14;
                            if (b.e) break block15;
                            v1 = b.b[var0];
                            ** GOTO lbl35
                        }
                        if (b.j.length() > 0) {
                            v2 = b.a(b.a("IGP-CATEGORIES"), var1_1[var7_7], b.j + "&ctg=XXXX");
                        }
                        break block16;
                    }
                    if (b.e) {
                        v2 = var1_1[var7_7].compareTo("GLDT") == 0 ? b.a(var3_3, var1_1[var7_7], b.e) : (var1_1[var7_7].compareTo("CATALOG") == 0 ? b.j : b.a(var3_3, var1_1[var7_7], var6_6));
                    } else {
                        v1 = b.b[var0] + "-" + var1_1[var7_7];
lbl35:
                        // 2 sources

                        v2 = var8_8 = b.a(v1);
                    }
                }
                if (!b.a(var8_8, 7)) continue;
                b.a[var0][var5_5] = var8_8;
                b.a[var0][var5_5++] = var7_7;
                b.b[var0][var7_7] = var2_2 + var7_7;
                continue;
            }
            catch (Exception v3) {}
        }
        if (var5_5 > 0) {
            b.a[4 + var0] = true;
            b.c[var0] = var5_5;
        }
    }

    private static String[] a(byte[] byArray) {
        String[] stringArray = new String[b.a(byArray)];
        for (int i = 0; i < stringArray.length; ++i) {
            int n = b.a(byArray);
            stringArray[i] = new String(byArray, y, n);
            y += n;
        }
        return stringArray;
    }

    private static void a(String[] stringArray) {
        int n = (stringArray.length - 1 > 0 ? stringArray.length - 1 : 0) + 4;
        f = ++n;
        g = f + 1;
        h = g + 1;
        i = h + 1;
        j = i + 1;
        k = j + 1;
        l = k + 1;
        m = l + 1;
        b.n = m + 1;
        o = b.n + 1;
        p = o + 1;
        q = p + 1;
        r = q + 1;
        s = r + 1;
        t = s + 1;
        u = t + c.length;
    }

    private static void b() {
        block57: {
            block59: {
                block58: {
                    block50: {
                        int n;
                        String[] stringArray;
                        int n2;
                        try {
                            n2 = b.b();
                            if (n2 == 0) {
                                m = false;
                                return;
                            }
                            byte[] byArray = b.a(0);
                            b.a(byArray);
                            a = b.a(byArray);
                            stringArray = b.a(byArray);
                            c = b.a(byArray);
                            d = b.a(byArray);
                            e = b.a(byArray);
                            a = b.a(byArray) == 1;
                            b = b.a(byArray) == 1;
                            try {
                                n = b.a(byArray);
                                c = new String(byArray, y, n);
                                if (c.equals((Object)"1.9z")) {
                                    ap = 2;
                                    J = 12;
                                    K = 6;
                                    B = 2;
                                    C = 4;
                                    D = 5;
                                }
                                c.startsWith(a);
                            }
                            catch (Exception exception) {
                                m = false;
                            }
                            b.a();
                        }
                        catch (Exception exception) {
                            m = false;
                            return;
                        }
                        b.a(stringArray);
                        H = stringArray.length;
                        I = H + 5;
                        g = new String[9];
                        a = new boolean[9];
                        for (n2 = 0; n2 < a.length; ++n2) {
                            b.a[n2] = false;
                        }
                        a = new String[3][];
                        a = new int[3][];
                        b = new int[3][];
                        c = new int[3];
                        if (d.j) {
                            c = true;
                        } else {
                            try {
                                String string = b.a("URL-ORANGE");
                                int n3 = Integer.parseInt((String)string);
                                if (!a && n3 == 1) {
                                    throw new RuntimeException("Trying load Orange France but Resources are not present on dataIGP\nHave you checked include Orange France option at IGPDataConfig.properties file?");
                                }
                                c = a && n3 == 1;
                            }
                            catch (Exception exception) {}
                        }
                        try {
                            e = b.a("URL-TEMPLATE-GAME").trim();
                            e = true;
                        }
                        catch (Exception exception) {}
                        for (int i = 0; i < H; ++i) {
                            b.a(i, stringArray[i], 7, "IGP-PROMOS", e);
                        }
                        String string = null;
                        try {
                            string = b.a("URL-OPERATOR");
                            if (b.a(string, 7)) {
                                j = string;
                            }
                            String string2 = b.a("URL-PT");
                            n = 0;
                            int n4 = 0;
                            if (string2.length() > 50) {
                                string2 = null;
                            }
                            if (string2 == null) break block50;
                            h = "";
                            int n5 = string2.length();
                            for (int i = 0; i < n5; ++i) {
                                block51: {
                                    String string3;
                                    StringBuffer stringBuffer;
                                    block53: {
                                        StringBuffer stringBuffer2;
                                        block56: {
                                            char c;
                                            block54: {
                                                block55: {
                                                    block52: {
                                                        c = string2.charAt(i);
                                                        if ((c < ' ' || c > 'z') && c != '\u0082' && c != '\n') break block51;
                                                        if (c == ' ') {
                                                            n4 = i;
                                                        }
                                                        if (i >= n5 - 1 || c != '\\' || string2.charAt(i + 1) != 'n' && string2.charAt(i + 1) != 'N') break block52;
                                                        if (h.length() > 0) {
                                                            if (n != 0) {
                                                                h = h + " ";
                                                            } else {
                                                                h = h + '\n';
                                                                n = 1;
                                                            }
                                                        }
                                                        ++i;
                                                        break block53;
                                                    }
                                                    if (c != '\n') break block54;
                                                    if (h.length() <= 0) break block53;
                                                    if (n == 0) break block55;
                                                    stringBuffer2 = new StringBuffer().append(h).append(" ");
                                                    break block56;
                                                }
                                                h = h + '\n';
                                                n = 1;
                                                break block53;
                                            }
                                            stringBuffer2 = new StringBuffer().append(h).append(c);
                                        }
                                        h = stringBuffer2.toString();
                                    }
                                    if (i != 26 || n != 0) continue;
                                    if (n4 == i) {
                                        stringBuffer = new StringBuffer().append(h);
                                        string3 = "\n";
                                    } else {
                                        stringBuffer = new StringBuffer().append(h.substring(0, n4)).append("\n");
                                        string3 = h.substring(n4 + 1, h.length());
                                    }
                                    h = stringBuffer.append(string3).toString();
                                    n = 1;
                                    continue;
                                }
                                h = null;
                                break;
                            }
                            if (h != null && !b.a(h = h.toUpperCase(), 7)) {
                                h = null;
                            }
                        }
                        catch (Exception exception) {}
                    }
                    if (!c) {
                        if (e) {
                            if (b.a(j, 7)) {
                                b.a(H, "PROMO", 7, "IGP-CATEGORIES", j + "&ctg=XXXX");
                            }
                        } else {
                            String string = b.a("URL-PROMO");
                            if (string != null) {
                                string.trim();
                                if (b.a(b.a("URL-PROMO"), 7)) {
                                    b.g[3] = string;
                                    b.a[3] = true;
                                }
                            }
                        }
                    }
                    b.a(0, c, t, "IGP-WN");
                    b.a(1, d, u, "IGP-BS");
                    if (c) break block57;
                    if (!e) break block58;
                    if (!b.a(b.a(b.a("IGP-CATEGORIES"), "OP", j), 7)) break block57;
                    b.g[6] = j;
                    if (!b.a(j, 7)) break block57;
                    break block59;
                }
                if (!b.a(j, 7)) break block57;
                b.g[6] = j;
            }
            b.a[6] = true;
        }
        if (c) {
            try {
                if (b.a(j, 7)) {
                    b.g[7] = j;
                    b.a[7] = true;
                }
            }
            catch (Exception exception) {}
        }
        try {
            String string;
            k = null;
            if (!e) {
                string = b.a("URL-GLIVE").trim();
            } else if (b.a(j, 7)) {
                string = k = b.a(b.a("IGP-CATEGORIES"), "GLIVE", j + "&ctg=XXXX");
            }
            if (b.a(k, 7) && b) {
                b.g[8] = k;
                b.a[8] = true;
            } else {
                b.g[8] = null;
                b.a[8] = false;
            }
        }
        catch (Exception exception) {
            b.g[8] = null;
            b.a[8] = false;
        }
        ac = b.b();
        if (ac > 0) {
            m = true;
        }
    }

    public static int a() {
        if (!m) {
            return -1;
        }
        if (a[8]) {
            if (b.b() > 1) {
                return 2;
            }
            return 1;
        }
        if (b.b() > 0) {
            return 0;
        }
        return -1;
    }

    public static boolean a() {
        return b.a() != -1;
    }

    public static void a(String string, int n) {
        block6: {
            int n2;
            block5: {
                block4: {
                    b.b(string, n);
                    if (d.b != 0) break block4;
                    n2 = 4 + H + 1 + 1 + 1 + 1 + 1 + 1;
                    break block5;
                }
                R = 5;
                if (d.b != 1) break block6;
                n2 = R;
            }
            R = n2 + 1;
        }
        b.f();
        O = b.c();
        if (k) {
            a.setCommandListener((CommandListener)a);
        }
    }

    private static void b(String string, int n) {
        if (n < 0 || n >= a.length) {
            return;
        }
        aj = n <= a.length ? n : 0;
        i = string;
        a = 0xFF0000;
        Q = -1;
        M = 0;
        P = -1;
        O = 0;
        V = 0;
        W = 0;
        b = new int[10];
        l = true;
        a = Font.getFont((int)0, (int)0, (int)8);
        c = al * 5 / 100;
        d = al / 2;
        e = al * 92 / 100;
        if (d.c == 2) {
            new Thread((Runnable)new b()).start();
        }
    }

    private static int b() {
        int n = 0;
        for (int i = 0; i < a.length; ++i) {
            if (!a[i]) continue;
            ++n;
        }
        return n;
    }

    private static int c() {
        for (int i = 0; i < a.length; ++i) {
            if (!a[i]) continue;
            return i;
        }
        return -1;
    }

    private static int b(int n, int n2) {
        if (n <= n2 - 1) {
            return n - 1;
        }
        if (n > I + n2 + 1 - 1) {
            return 12;
        }
        if ((n -= n2) < H) {
            return 4;
        }
        if ((n -= H) == 0) {
            return 5;
        }
        return 7 + n - 1;
    }

    private static void a(int n) {
        byte[] byArray = null;
        y = 0;
        int n2 = b.b(n, 5);
        int n3 = n - 1;
        int n4 = n - 5;
        if (n4 > 0 && n < I + 4) {
            if (n == 0 && !a[n4]) {
                return;
            }
            b.c[n4] = b[10];
        }
        switch (n2) {
            case -1: {
                b = new Image[w];
                c = new Image[9];
                a = new Image[3][];
                b.a[0] = new Image[c.length];
                b.a[1] = new Image[d.length];
                b.a[2] = new Image[e.length];
                return;
            }
            case 0: {
                b.b();
                return;
            }
            case 1: {
                int n5;
                int n6;
                byArray = b.a(n3);
                for (n6 = 0; n6 < aj; ++n6) {
                    n5 = b.a(byArray);
                    y += n5;
                }
                b.a(byArray);
                n5 = b.a(byArray);
                f = new String[n5];
                byte[] byArray2 = new byte[n5];
                System.arraycopy((Object)byArray, (int)y, (Object)byArray2, (int)0, (int)n5);
                y += n5;
                b.a(byArray);
                int n7 = byArray[y++] & 0xFF | (byArray[y++] & 0xFF) << 8;
                a = new short[n7];
                for (n6 = 0; n6 < n7 - 1; ++n6) {
                    b.a[n6] = (short)((byArray[y++] & 0xFF) + ((byArray[y++] & 0xFF) << 8));
                }
                b.a[n7 - 1] = (short)n5;
                for (n6 = 0; n6 < n7; ++n6) {
                    Exception exception;
                    int n8 = n6 == 0 ? 0 : a[n6 - 1] & 0xFFFF;
                    int n9 = (a[n6] & 0xFFFF) - n8;
                    if (n9 == 0) continue;
                    try {
                        if (d.e) {
                            b.f[n6] = new String(byArray2, n8, n9, "UTF-8");
                            continue;
                        }
                        exception = new StringBuffer(n9 / 2 + 2);
                        int n10 = n8;
                        while (n10 < n8 + n9) {
                            if ((byArray2[n10] & 0x80) == 0) {
                                exception.append((char)(byArray2[n10++] & 0xFF));
                            } else if ((byArray2[n10] & 0xE0) == 192) {
                                if (n10 + 1 >= n8 + n9 || (byArray2[n10 + 1] & 0xC0) != 128) {
                                    throw new Exception();
                                }
                                exception.append((char)((byArray2[n10++] & 0x1F) << 6 | byArray2[n10++] & 0x3F));
                            } else if ((byArray2[n10] & 0xF0) == 224) {
                                if (n10 + 2 >= n8 + n9 || (byArray2[n10 + 1] & 0xC0) != 128 || (byArray2[n10 + 2] & 0xC0) != 128) {
                                    throw new Exception();
                                }
                                exception.append((char)((byArray2[n10++] & 0xF) << 12 | (byArray2[n10++] & 0x3F) << 6 | byArray2[n10++] & 0x3F));
                            } else {
                                throw new Exception();
                            }
                            b.f[n6] = exception.toString().toUpperCase();
                        }
                        continue;
                    }
                    catch (Exception exception2) {
                        exception = exception2;
                        exception2.printStackTrace();
                    }
                }
                if (!k) break;
                a = new Command(b.a(j), 4, 1);
                b = new Command(b.a(k), 2, 1);
                b.a(true, true);
                return;
            }
            case 2: {
                Image image;
                int n11;
                Image[] imageArray;
                a = new Image[2];
                byArray = b.a(n3);
                int n12 = b.a(byArray);
                y = 0;
                b.a[0] = b.a(byArray);
                if (d.b) {
                    imageArray = a;
                    n11 = 1;
                    image = b.b(byArray, 2, n12, 1, 0xFF0000);
                } else {
                    imageArray = a;
                    n11 = 1;
                    image = a[0];
                }
                imageArray[n11] = image;
                int n13 = b.a(byArray);
                int n14 = b.a(byArray);
                a = new byte[(n14 + 1) * (4 + ap)];
                int n15 = n13 / (6 + ap);
                for (int i = 0; i < n15; ++i) {
                    int n16 = b.a(byArray);
                    System.arraycopy((Object)byArray, (int)y, (Object)a, (int)(n16 *= 4 + ap), (int)(4 + ap));
                    y += 4 + ap;
                }
                z = a[32 * (4 + ap) + D];
                return;
            }
            case 3: {
                byArray = b.a(n3);
                for (int i = 0; i < w; ++i) {
                    if (!d.h && (i == 13 || i == 12)) continue;
                    b.b[i] = b.a(byArray);
                }
                if (c == null) break;
                b.b[9] = b;
                b.b[8] = c;
                return;
            }
            case 12: {
                b.a();
                return;
            }
            default: {
                int n17 = y;
                int n18 = x;
                y = n17;
                x = n18;
                b.a(n2, n3, n4);
            }
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void a(int var0, int var1_1, int var2_2) {
        var3_3 = null;
        var4_4 = 0;
        var5_5 = 0;
        switch (var0) {
            case 4: 
            case 6: {
                v0 = b.c;
                v1 = var2_2;
                v2 = b.a(b.a(var1_1));
                ** GOTO lbl59
            }
            case 5: {
                var3_3 = b.a(var1_1);
                b.e = b.a(var3_3);
                return;
            }
            case 7: {
                var5_5 = b.c.length - 1;
            }
            case 8: {
                if (var0 == 8) {
                    var5_5 = b.d.length - 1;
                }
                var4_4 = var0 - 7;
                var3_3 = b.a(var1_1);
                for (var6_6 = 0; var6_6 < var5_5; ++var6_6) {
                    b.a[var4_4][var6_6] = b.a(var3_3);
                }
                v0 = b.a[var4_4];
                v1 = var6_6;
                v2 = b.b[11];
                ** GOTO lbl59
            }
            case 9: {
                var1_1 = b.v = 4 + b.H;
                var3_3 = b.a(var1_1);
                v0 = b.c;
                v1 = var2_2;
                v3 = var3_3;
                v4 = 2;
                v5 = var3_3.length - 2;
                v6 = 0xFF3300;
                v7 = 22923;
                ** GOTO lbl58
            }
            case 10: {
                if (!b.c) break;
                var7_7 = b.x - 2;
                var3_3 = b.a(var7_7);
                b.c[var2_2] = b.a(var3_3);
                b.d = b.a(var3_3);
                return;
            }
            case 11: {
                var7_8 = b.x - 1 - (b.a != false ? 2 : 1);
                var3_3 = b.a(var7_8);
                b.a = b.a(var3_3);
                var3_3 = b.a(4 + b.H);
                v0 = b.c;
                v1 = 8;
                v3 = var3_3;
                v4 = 2;
                v5 = var3_3.length - 2;
                v6 = 0xFF3300;
                v7 = 16760064;
lbl58:
                // 2 sources

                v2 = b.a(v3, v4, v5, v6, v7);
lbl59:
                // 3 sources

                v0[v1] = v2;
            }
        }
    }

    private static void b(boolean bl) {
        int n;
        e = null;
        for (n = 0; n < a.length; ++n) {
            if (a[n] == null) continue;
            for (int i = 0; i < a[n].length; ++i) {
                b.a[n][i] = null;
            }
        }
        for (n = 0; n < c.length; ++n) {
            b.c[n] = null;
        }
        a = null;
        if (bl) {
            b.a();
            a = null;
            a = null;
            for (n = 0; n < w; ++n) {
                b.b[n] = null;
            }
            b = null;
            a = null;
            f = null;
            b = null;
            i = null;
            c = null;
            d = null;
            a = null;
            b = null;
            c = null;
        }
        System.gc();
    }

    public static void a(boolean bl) {
        if (bl) {
            if (M == 0 || M == 2) {
                P = M;
                M = 5;
                return;
            }
        } else if (M == 5) {
            M = P;
            Q = -1;
        }
    }

    private static int a(byte[] byArray, int n, int n2, String string) {
        for (int i = n; i < n2 - 4; ++i) {
            if ((byArray[i] & 0xFF) != string.charAt(0) || (byArray[i + 1] & 0xFF) != string.charAt(1) || (byArray[i + 2] & 0xFF) != string.charAt(2) || (byArray[i + 3] & 0xFF) != string.charAt(3)) continue;
            return i;
        }
        return -1;
    }

    private static Image a(byte[] byArray, int n, int n2, int n3, int n4) {
        int n5;
        int[] nArray = new int[10];
        int[] nArray2 = new int[10];
        int n6 = 0;
        for (n5 = 0; n5 < nArray.length; ++n5) {
            nArray[n5] = -1;
            nArray2[n5] = -1;
        }
        n5 = b.a(byArray, n, n2, "PLTE");
        int n7 = b.a(byArray, n, n2, "tRNS");
        Image image = null;
        if (n5 > 0 && n7 > 0) {
            long l;
            int n8;
            int n9;
            int n10;
            int n11;
            int n12 = (byArray[n5 - 4] << 24 & 0xFF000000) + (byArray[n5 - 3] << 16 & 0xFF0000) + (byArray[n5 - 2] << 8 & 0xFF00) + (byArray[n5 - 1] << 0 & 0xFF);
            boolean bl = false;
            for (n11 = 0; n11 < n12 / 3; ++n11) {
                if (byArray[n7 + 4 + n11] == 0) continue;
                n10 = byArray[n5 + 4 + 3 * n11] & 0xFF;
                n9 = byArray[n5 + 4 + 3 * n11 + 1] & 0xFF;
                n8 = byArray[n5 + 4 + 3 * n11 + 2] & 0xFF;
                if (n10 == 255 || n9 == 255 || n8 == 255) {
                    bl = true;
                    break;
                }
                if (n10 != 0 && n9 != 0 && n8 != 0) continue;
                bl = true;
                break;
            }
            if (!bl) {
                n11 = (n3 & 0xFF0000) >> 24 & 0xFF;
                n10 = (n3 & 0xFF0000) >> 16 & 0xFF;
                n9 = (n3 & 0xFF00) >> 8 & 0xFF;
                n8 = n3 & 0xFF;
                n10 = n10 == 255 ? 254 : n10;
                n9 = n9 == 255 ? 254 : n9;
                n8 = n8 == 255 ? 254 : n8;
                n10 = n10 == 0 ? 1 : n10;
                n9 = n9 == 0 ? 1 : n9;
                n8 = n8 == 0 ? 1 : n8;
                n3 = 0 | (n11 & 0xFF) << 24;
                n3 |= (n10 & 0xFF) << 16;
                n3 |= (n9 & 0xFF) << 8;
                n3 |= n8 & 0xFF;
            }
            for (n11 = 0; n11 < n12 / 3; ++n11) {
                if (byArray[n7 + 4 + n11] == 0 || (byArray[n5 + 4 + 3 * n11] & 0xFF) != ((n3 & 0xFF0000) >> 16 & 0xFF) || (byArray[n5 + 4 + 3 * n11 + 1] & 0xFF) != ((n3 & 0xFF00) >> 8 & 0xFF) || (byArray[n5 + 4 + 3 * n11 + 2] & 0xFF) != (n3 & 0xFF)) continue;
                nArray[n6] = n11;
                n10 = b.a(byArray, n5 + 4 + 3 * n11, 3);
                b.a(byArray, n5 + 4 + 3 * n11, 3, n4);
                nArray2[n6] = n10;
                ++n6;
            }
            byte[] byArray2 = new byte[n12 + 4];
            System.arraycopy((Object)byArray, (int)n5, (Object)byArray2, (int)0, (int)(n12 + 4));
            long[] lArray = new long[256];
            for (n9 = 0; n9 < 256; ++n9) {
                l = n9;
                for (n8 = 0; n8 < 8; ++n8) {
                    l = (l & 1L) == 1L ? 0xEDB88320L ^ l >> 1 : l >> 1;
                }
                lArray[n9] = l;
            }
            l = 0xFFFFFFFFL;
            for (n9 = 0; n9 < byArray2.length; ++n9) {
                l = lArray[(int)(l ^ (long)byArray2[n9]) & 0xFF] ^ l >> 8;
            }
            n9 = b.a(byArray, n5 + 4 + n12, 4);
            b.a(byArray, n5 + 4 + n12, 4, (int)(l ^= 0xFFFFFFFFL));
            System.gc();
            if (d.d) {
                byte[] byArray3 = new byte[n2];
                System.arraycopy((Object)byArray, (int)n, (Object)byArray3, (int)0, (int)n2);
                byArray = byArray3;
                n = 0;
            }
            image = Image.createImage((byte[])byArray, (int)n, (int)n2);
            for (int i = 0; i < n6; ++i) {
                int n13 = nArray[i];
                int n14 = nArray2[i];
                b.a(byArray, n5 + 4 + 3 * n13, 3, n14);
            }
            b.a(byArray, n5 + 4 + n12, 4, n9);
        }
        return image;
    }

    private static void a(byte[] byArray, int n, int n2, int n3) {
        for (int i = n2 - 1; i >= 0; --i) {
            byArray[n + n2 - 1 - i] = (byte)((n3 & 255 << 8 * i) >> 8 * i);
        }
    }

    private static int a(byte[] byArray, int n, int n2) {
        int n3 = 0;
        for (int i = n2 - 1; i >= 0; --i) {
            n3 += byArray[n + n2 - 1 - i] << 8 * i & 255 << 8 * i;
        }
        return n3;
    }

    /*
     * Unable to fully structure code
     */
    public static boolean a(int var0) {
        if (!b.m) {
            return true;
        }
        if (d.h && b.p) {
            b.p = false;
        } else {
            b.N = var0;
        }
        switch (b.M) {
            case 0: {
                if (b.Q >= b.R) {
                    b.M = 1;
                    b.c();
                    if (d.b == 0) {
                        for (var1_1 = 0; var1_1 < b.c.length; ++var1_1) {
                            if (b.c == null || b.c[var1_1] == null) continue;
                            var2_4 = b.c[var1_1].getWidth();
                            if (var2_4 > b.ak) {
                                throw new RuntimeException("IGP::Page " + var1_1 + " image width bigger than Screen width(" + b.ak + ")");
                            }
                            var3_7 = b.c[var1_1].getHeight();
                            if (var3_7 <= b.al) continue;
                            throw new RuntimeException("IGP::Page " + var1_1 + " image height bigger than Screen height(" + b.al + ")");
                        }
                    } else if (b.c != null && b.c[b.O] != null) {
                        var1_2 = b.c[b.O].getWidth();
                        if (var1_2 > b.ak) {
                            throw new RuntimeException("IGP::Page " + b.O + " image width bigger than Screen width(" + b.ak + ")");
                        }
                        var2_5 = b.c[b.O].getHeight();
                        if (var2_5 > b.al) {
                            throw new RuntimeException("IGP::Page " + b.O + " image height bigger than Screen height(" + b.al + ")");
                        }
                    }
                } else {
                    b.a(d.b != 0 && b.Q == 6 ? b.I + 5 - 1 : b.Q);
                }
                ++b.Q;
                break;
            }
            case 1: {
                switch (b.N) {
                    case 26: {
                        v0 = 4;
                        ** GOTO lbl85
                    }
                    case 23: {
                        if (b.ac <= 1) break;
                        if (b.O != 0) ** GOTO lbl43
                        v1 = 8;
                        ** GOTO lbl46
lbl43:
                        // 1 sources

                        v2 = b.O;
                        block22: while (true) {
                            v1 = v2 - 1;
                            while (!b.a[b.O = v1]) {
                                if (b.O == 0) {
                                    v1 = 8;
                                    continue;
                                }
                                v2 = b.O;
                                continue block22;
                            }
                            break;
                        }
                        b.f = true;
                    }
                    case 24: {
                        if (b.ac <= 1) break;
                        if (b.f) ** GOTO lbl71
                        if (b.O != 8) ** GOTO lbl60
                        v3 = 0;
                        ** GOTO lbl63
lbl60:
                        // 1 sources

                        v4 = b.O;
                        block24: while (true) {
                            v3 = v4 + 1;
                            while (!b.a[b.O = v3]) {
                                if (b.O == 8) {
                                    v3 = 0;
                                    continue;
                                }
                                v4 = b.O;
                                continue block24;
                            }
                            break;
                        }
                        b.g = true;
lbl71:
                        // 2 sources

                        b.V = 0;
                        b.W = 0;
                        b.c();
                        break;
                    }
                    case 32: {
                        if (!b.o || b.W >= b.T - 1 || ++b.W - b.V < b.U) break;
                        ++b.V;
                        break;
                    }
                    case 21: {
                        if (!b.o || b.W <= 0 || --b.W - b.V >= 0) break;
                        --b.V;
                        break;
                    }
                    case 25: 
                    case 27: {
                        v0 = 6;
lbl85:
                        // 2 sources

                        b.M = v0;
                    }
                }
                break;
            }
            case 6: {
                var1_3 = null;
                var1_3 = b.g[b.O];
                if (b.o) {
                    var1_3 = b.a[b.S][b.W];
                }
                if (var1_3 == null || var1_3.length() <= 0) break;
                if (d.c == 2) {
                    b.g = var1_3;
                    break;
                }
                b.d = var1_3;
                break;
            }
            case 2: {
                b.b(false);
                if (d.b == 1) {
                    b.b();
                }
                b.Q = 5 + b.O;
                b.a(b.Q);
                if (b.c != null && b.c[b.O] != null) {
                    var2_6 = b.c[b.O].getWidth();
                    if (var2_6 > b.ak) {
                        throw new RuntimeException("IGP::Page " + b.O + " image width bigger than Screen width(" + b.ak + ")");
                    }
                    var3_8 = b.c[b.O].getHeight();
                    if (var3_8 > b.al) {
                        throw new RuntimeException("IGP::Page " + b.O + " image height bigger than Screen height(" + b.al + ")");
                    }
                }
                if (d.b == 1) {
                    b.a();
                }
                b.M = 1;
                break;
            }
            case 5: {
                break;
            }
            case 3: {
                switch (b.N) {
                    case 26: {
                        b.M = 1;
                        b.f = null;
                        break;
                    }
                    case 25: 
                    case 27: {
                        if (d.c == 2) {
                            b.g = b.f;
                            break;
                        }
                        b.d = b.f;
                    }
                }
                break;
            }
            case 4: {
                b.b(true);
                if (b.k) {
                    b.a.setCommandListener(b.a);
                    b.e();
                }
                b.l = false;
                return true;
            }
        }
        return false;
    }

    private static void c() {
        if (d.b == 1) {
            M = 2;
        }
        a = 0;
        ad = O;
        W = 0;
        T = 0;
        V = 0;
        o = false;
        boolean bl = n = g[O] != null && g[O].length() > 0 && g[O].compareTo("DEL") != 0;
        if (O == 4) {
            S = 0;
            o = true;
            n = false;
        }
        if (O == 5) {
            S = 1;
            o = true;
            n = false;
        }
        if (O == 6 || O == 7) {
            n = true;
        }
        if (n || o) {
            a = (byte)(a | 1);
        }
        a = (byte)(a | 2);
        int n = ae = d.h ? l : h;
        if (O == 0 || O == 1 || O == 2) {
            int n2 = ae = d.h ? m : i;
        }
        if (o) {
            T = c[S];
            int n3 = ae = d.h ? m : i;
            if (O == 6) {
                b.n = true;
                int n4 = ae = d.h ? l : h;
            }
        }
        if (O == 8) {
            a = (byte)(a | 3);
        }
    }

    /*
     * Unable to fully structure code
     */
    public static void a(Graphics var0) {
        if (!b.m) {
            return;
        }
        if (b.d != null && d.c == 1) {
            b.g();
            return;
        }
        var1_1 = var0;
        b.b(var0, 0, 0, b.ak, b.al);
        b.b(var1_1, 0, 0, b.ak, b.al);
        switch (b.M) {
            case 0: {
                var0.setColor(0);
                var0.fillRect(0, 0, b.ak, b.al);
                b.a(var0, b.an, b.ak * 3 / 4, b.Q, b.R);
                if (b.i == null) break;
                if (b.i.trim().equals((Object)"")) {
                    return;
                }
                var0.setColor(0xFFFFFF);
                var0.setFont(b.a);
                var0.drawString(b.i, b.am, b.an - 5, 33);
                return;
            }
            case 1: {
                b.d();
                if (d.j) {
                    var2_2 = 0;
                    v0 = 0;
                } else {
                    var2_2 = 201756;
                    v0 = var3_3 = 35031;
                }
                if (b.O == 3) {
                    var2_2 = 201756;
                    var3_3 = 11980248;
                }
                if (b.O == 6) {
                    var2_2 = 201756;
                    var3_3 = 11980248;
                }
                if (b.O == 7) {
                    var2_2 = 0;
                    var3_3 = 0;
                }
                if (b.O == 8) {
                    var1_1.setColor(39423);
                    var1_1.fillRect(0, 0, b.ak, b.al);
                } else {
                    b.a(var1_1, 0, 0, b.ak, b.al, var2_2, var3_3);
                }
                b.d(var1_1);
                if (!b.o) ** GOTO lbl47
                b.b(var1_1);
                ** GOTO lbl176
lbl47:
                // 1 sources

                if (b.O != 7) ** GOTO lbl84
                if (d.j) {
                    var4_4 = b.ak / 2;
                    var5_6 = b.al * 8 / 100;
                    v1 = var1_1;
                    v2 = b.d;
                    v3 = var4_4;
                    v4 = var5_6;
                    v5 = 17;
                } else {
                    var4_4 = b.ak * 9 / 100;
                    var5_6 = b.al - b.b[8].getHeight() - 5;
                    if (d.h) {
                        var5_6 -= b.b[12].getHeight();
                    }
                    v1 = var1_1;
                    v2 = b.d;
                    v3 = b.ak - var4_4;
                    v4 = var5_6;
                    v5 = 40;
                }
                b.a(v1, v2, v3, v4, v5);
                b.d = true;
                b.a(b.f, null, 0, 0, 0);
                var6_7 = b.F;
                var7_8 = b.ai - b.c[b.O].getHeight();
                var8_9 = Math.abs((int)((var7_8 - var6_7) / 3));
                v6 = var8_9 = var8_9 < 3 ? 3 : var8_9;
                if (!d.j) ** GOTO lbl80
                v7 = b.a(b.g);
                v8 = var1_1;
                v9 = b.ak - (b.b[4].getWidth() + 8) * 2;
                v10 = b.ak / 2;
                v11 = b.al * 60 / 100;
                ** GOTO lbl174
lbl80:
                // 1 sources

                b.a(b.a(b.f), var1_1, b.ak - (b.b[4].getWidth() + 8) * 2, b.b[4].getWidth() + 8, b.c[b.O].getHeight() + var8_9, 20);
                b.ai = b.c[b.O].getHeight() + var8_9 + b.F + b.ag / 2 + var8_9;
                b.a(var1_1, b.c[b.O], b.am, 2, 17);
                ** GOTO lbl176
lbl84:
                // 1 sources

                if (b.O != 3) ** GOTO lbl111
                var4_4 = b.al >= 128 ? 1 : 0;
                var5_6 = b.h != null && b.h.length() > 0 ? 1 : 0;
                var6_7 = var4_4 != 0 ? b.b[10].getHeight() : 0;
                var7_8 = b.e.getHeight();
                var8_9 = var5_6 != 0 ? b.z * 3 : 0;
                var9_10 = var7_8 + var8_9 + (b.al - b.ai);
                var10_14 = Math.max((int)0, (int)(b.al - var9_10));
                var11_18 = var10_14 / 3;
                var11_18 = Math.max((int)2, (int)var11_18);
                if (var4_4 != 0) {
                    b.a(var1_1, b.b[10], b.am, b.c, 17);
                }
                var12_21 = var11_18 + var6_7;
                var12_21 = var5_6 != 0 ? var12_21 + b.e.getHeight() / 2 : b.al / 2;
                b.a(var1_1, b.e, b.am - 1, var12_21, 3);
                b.a(b.a(b.ad), var1_1, b.e.getWidth() * 9 / 20, b.am + 2, var12_21, 3);
                var12_21 += b.e.getHeight() / 2;
                if (var5_6 == 0) ** GOTO lbl176
                b.E = 1;
                var13_23 = b.ai - var12_21 - b.b[8].getHeight();
                v7 = b.h;
                v8 = var1_1;
                v9 = b.ak;
                v10 = b.am;
                v12 = var12_21;
                v13 = var13_23;
                ** GOTO lbl173
lbl111:
                // 1 sources

                if (b.O == 6) {
                    var4_4 = b.al >= 128 ? 1 : 0;
                    if (var4_4 != 0) {
                        b.b[10].getHeight();
                    }
                    var5_6 = 0;
                    var6_7 = b.c[b.O].getHeight();
                    var7_8 = var6_7 + (b.al - b.ai);
                    var8_9 = Math.max((int)0, (int)(b.al - var7_8));
                    var9_11 = var8_9 / 4;
                    Math.max((int)2, (int)var9_11);
                    if (var4_4 != 0) {
                        b.a(var1_1, b.b[10], b.am, b.c, 17);
                    }
                    var10_15 = b.al / 2;
                    b.a(var1_1, b.c[b.O], b.am, var10_15, 3);
                    var11_19 = b.E;
                    b.E = 1;
                    b.a(b.a(b.ad), var1_1, b.c[b.O].getWidth() / 2, b.am, var10_15, 3);
                    b.E = var11_19;
                } else {
                    if (b.O == 8) {
                        var4_4 = b.a.getHeight();
                        var5_6 = b.c[8].getHeight();
                        var6_7 = 0;
                        b.d = true;
                        b.a(b.a(b.p), var1_1, b.ak - 50, b.am, 0, 17);
                        var7_8 = b.F;
                        b.d = true;
                        b.a(b.a(b.q), var1_1, b.ak - 50, b.am, 0, 17);
                        var8_9 = b.F;
                        var9_12 = b.al - var4_4 - b.ag - var7_8 - var8_9 - var5_6;
                        var10_16 = var9_12 / 6;
                        b.a(var1_1, b.a, b.am, 0, 17);
                        var6_7 = 0 + (var4_4 + var10_16);
                        b.E = 0;
                        b.a(b.a(b.p), var1_1, b.ak * 3 / 4, b.am, var6_7, 17);
                        b.a(var1_1, b.c[8], b.am - 1, var6_7 += var7_8 + var10_16, 17);
                        b.a(b.a(b.r), var1_1, b.ak * 3 / 4, b.am, var6_7 + var5_6 / 2, 3);
                        v7 = b.a(b.q);
                        v8 = var1_1;
                        v9 = b.ak * 3 / 4;
                        v10 = b.am;
                        v11 = (var6_7 += var5_6 + var10_16) - 2;
                        v14 = 17;
                    } else {
                        var4_4 = b.c[b.O].getHeight();
                        var5_6 = b.z * 2;
                        var6_7 = var4_4 + var5_6;
                        var7_8 = Math.max((int)0, (int)(b.al - var6_7));
                        var8_9 = var7_8 / 4;
                        var9_13 = var8_9 = Math.max((int)0, (int)var8_9);
                        var10_17 = var8_9;
                        b.a(var1_1, b.c[b.O], b.am, var10_17, 17);
                        var11_20 = b.k != false ? b.ak : b.ak - (b.b[9].getWidth() + b.b[8].getWidth());
                        var12_22 = b.al - 2 - (var9_13 += var4_4 + (d.h != false ? 0 : var8_9)) - (d.h != false ? b.b[12].getHeight() : 0);
                        v7 = b.a(b.ad);
                        v8 = var1_1;
                        v9 = var11_20;
                        v10 = b.am;
                        v12 = var9_13;
                        v13 = var12_22;
lbl173:
                        // 2 sources

                        v11 = v12 + v13 / 2;
lbl174:
                        // 2 sources

                        v14 = 3;
                    }
                    b.a(v7, v8, v9, v10, v11, v14);
                }
lbl176:
                // 5 sources

                if (b.ac > 1) {
                    var4_4 = Math.abs((int)((int)(System.currentTimeMillis() / 80L % 8L) - 4));
                    var5_6 = 5;
                    var6_7 = 7;
                    var7_8 = 1;
                    var8_9 = 3;
                    if (b.f || d.h && b.ao == 23) {
                        var5_6 = 4;
                        var7_8 = 0;
                        ++b.L;
                    }
                    if (b.g || d.h && b.ao == 24) {
                        var6_7 = 6;
                        var8_9 = 2;
                        ++b.L;
                    }
                    b.a(var1_1, b.b[var5_6], 1 + var4_4, b.an, 6);
                    if (!d.h && !d.k) {
                        b.a(var1_1, b.b[var7_8], 1 + var4_4 + b.J, b.an, 6);
                    }
                    b.a(var1_1, b.b[var6_7], b.ak - 1 - var4_4, b.an, 10);
                    if (!d.h && !d.k) {
                        b.a(var1_1, b.b[var8_9], b.ak - 1 - var4_4 - (b.b[var6_7].getWidth() - b.b[var8_9].getWidth()) + b.K, b.an, 10);
                    }
                    if (b.L > 4) {
                        b.f = false;
                        b.g = false;
                        b.L = 0;
                    }
                }
                if (System.currentTimeMillis() % 1000L <= 500L && (b.ao != 27 || b.q)) break;
                b.c(var0);
                return;
            }
            case 2: {
                var0.setFont(b.a);
                var4_5 = b.a.getHeight();
                var0.setColor(255);
                var0.fillRect(0, b.an - var4_5 - 5, b.ak, var4_5 * 2);
                var0.setColor(0xFFFFFF);
                var0.drawString(b.i, b.am, b.an, 65);
                return;
            }
            case 5: {
                return;
            }
            case 3: {
                b.a(var0, 0, 0, b.ak, b.al, 201756, 35031);
                b.a(b.s, var0, b.am, b.an, 33);
                b.d(var0);
            }
        }
    }

    private static void b(Graphics graphics) {
        int n;
        int n2;
        int n3;
        int n4;
        int n5 = c;
        if (al > 128) {
            b.a(graphics, c[O], am, c, 17);
            n5 += c[O].getHeight();
        }
        int n6 = n5;
        E = 1;
        b.a(ad, graphics, am, n6, 17);
        int n7 = Math.max((int)(2 * z), (int)a[S][a[S][0]].getHeight());
        d = true;
        b.a(ad, null, 0, 0, 0);
        int n8 = n6 + F;
        int n9 = n4 = al * 5 / 100;
        int n10 = (al / 2 - n8) * 2;
        int n11 = al - b[8].getHeight() - 2 - n8;
        U = T;
        if (n10 / n7 >= T) {
            n3 = n8;
            n2 = n10;
        } else {
            if (n11 / n7 < T) {
                U = (n11 - 2 * n9) / n7;
            }
            n3 = n8;
            n2 = n11;
        }
        int n12 = n8 = n3 + n2 / 2 - U * n7 / 2;
        if (U < T) {
            if (V > 0) {
                b.a(graphics, am, n12 - n9, n4, 65535, true, false);
            }
            if (V + U < T) {
                b.a(graphics, am, n12 + U * n7 + n9, n4, 65535, true, true);
            }
        }
        n12 = n8 + n7 / 2 + 1;
        int n13 = n = n4 + b[5].getWidth();
        int n14 = ak * 1 / 100;
        int n15 = n13 + a[S][0].getWidth() + n14;
        for (int i = V; i < V + U; ++i) {
            int n16 = a[S][i];
            b.a(graphics, a[S][n16], n13, n12, 6);
            if (S == 2 || n16 == b[S].length - 1) {
                E = 1;
            }
            b.a(b.a(b[S][n16]), graphics, n15, n12, 6);
            n12 += n7;
        }
        X = W - V;
        Y = n13 - 2;
        Z = n8 + n7 * X;
        aa = ak - Y - n + 2;
        ab = n7;
        graphics.setColor(0xFFFFFF);
        graphics.drawRect(Y, Z, aa, ab);
    }

    private static void a(Graphics graphics, int n, int n2, int n3, int n4, boolean bl, boolean bl2) {
        int n5;
        int n6;
        int n7;
        int n8;
        int n9;
        int n10;
        int n11;
        Graphics graphics2;
        int n12;
        int n13;
        int n14;
        int n15;
        int n16;
        int n17;
        int n18;
        Graphics graphics3;
        int n19;
        int n20 = n19 = bl2 ? -1 : 1;
        if (n3 % 2 == 0) {
            --n3;
        }
        graphics.setColor(0xFFFFFF);
        if (bl) {
            graphics3 = graphics;
            n18 = n;
            n17 = n2;
            n16 = n - (n3 >> 1);
            n15 = n2 + n19 * (n3 >> 1);
            n14 = n + (n3 >> 1);
            n13 = n2;
            n12 = n19 * (n3 >> 1);
        } else {
            graphics3 = graphics;
            n18 = n;
            n17 = n2;
            n16 = n - n19 * (n3 >> 1);
            n15 = n2 - (n3 >> 1);
            n14 = n - n19 * (n3 >> 1);
            n13 = n2;
            n12 = n3 >> 1;
        }
        b.b(graphics3, n18, n17, n16, n15, n14, n13 + n12);
        graphics.setColor(n4);
        if (bl) {
            graphics2 = graphics;
            n11 = n;
            n10 = n2 + n19;
            n9 = n - (n3 >> 1) + 2;
            n8 = n2 + n19 * (n3 >> 1) - n19;
            n7 = n + (n3 >> 1) - 2;
            n6 = n2 + n19 * (n3 >> 1);
            n5 = n19;
        } else {
            graphics2 = graphics;
            n11 = n - n19;
            n10 = n2;
            n9 = n - n19 * (n3 >> 1) + n19;
            n8 = n2 - (n3 >> 1) + 2;
            n7 = n - n19 * (n3 >> 1) + n19;
            n6 = n2 + (n3 >> 1);
            n5 = 2;
        }
        b.b(graphics2, n11, n10, n9, n8, n7, n6 - n5);
    }

    /*
     * Unable to fully structure code
     */
    private static void d() {
        b.d = true;
        b.a(b.ae, null, 0, 0, 3);
        var0 = b.a(32, b.C) / 2;
        var1_1 = b.a(32, b.D) / 3;
        b.af = b.G + var0;
        b.ag = b.F + var1_1;
        if ((b.F + b.ag) % 2 != 0) {
            ++b.ag;
        }
        b.ah = b.am - b.af / 2;
        switch (b.O) {
            case 0: 
            case 1: 
            case 2: 
            case 7: {
                v0 = b.d;
                ** GOTO lbl16
            }
            case 3: 
            case 6: 
            case 8: {
                v0 = b.e;
lbl16:
                // 2 sources

                b.ai = v0 - b.ag / 2;
            }
        }
        if (d.j && b.O == 7) {
            b.ai = b.al * 80 / 100;
        }
    }

    private static void c(Graphics graphics) {
        if (n) {
            graphics.setColor(a);
            if (d.j) {
                graphics.setColor(0xFF7F00);
            }
            if (!q && ao == 27) {
                graphics.setColor(14588928);
                graphics.drawRect(ah - 2, ai - 2, af + 3, ag + 4);
                graphics.drawRect(ah - 1, ai - 1, af + 1, ag + 2);
                graphics.setColor(5767410);
            }
            E = 0;
            graphics.fillRect(ah, ai, af, ag + 1);
            b.a(ae, graphics, am, ai + (ag >> 1), 3);
        }
    }

    /*
     * Unable to fully structure code
     */
    private static void d(Graphics var0) {
        block15: {
            block16: {
                block14: {
                    block11: {
                        block13: {
                            block12: {
                                var1_1 = b.b;
                                var2_2 = b.al - 2;
                                var3_3 = var1_1;
                                var4_4 = b.ak - var1_1;
                                if (b.k) {
                                    return;
                                }
                                if (!d.h) break block11;
                                var5_5 = b.b[12];
                                var6_6 = b.b[12];
                                if (b.ao != 26) break block12;
                                if (d.a) ** GOTO lbl-1000
                                var5_5 = b.b[13];
                                break block13;
                            }
                            if (b.ao == 25 && b.q) {
                                ** if (!d.a) goto lbl-1000
lbl-1000:
                                // 1 sources

                                {
                                    var5_5 = b.b[13];
                                    ** GOTO lbl21
                                }
                            }
                            break block13;
lbl-1000:
                            // 2 sources

                            {
                                var6_6 = b.b[13];
                            }
                        }
                        b.a(var0, var5_5, var1_1, var2_2, 36);
                        b.a(var0, var6_6, b.ak - var1_1, var2_2, 40);
                        var3_3 += b.b[12].getWidth() / 2 - b.b[9].getWidth() / 2;
                        var4_4 += -b.b[12].getWidth() / 2 + b.b[8].getWidth() / 2;
                        var2_2 += -b.b[12].getHeight() / 2 + b.b[9].getHeight() / 2;
                    }
                    if (!d.a) break block14;
                    if ((b.a & 1) != 0) {
                        b.a(var0, b.b[9], var3_3, var2_2, 36);
                    }
                    if ((b.a & 2) == 0) break block15;
                    v0 = var0;
                    v1 = b.b;
                    v2 = 8;
                    break block16;
                }
                if ((b.a & 2) != 0) {
                    b.a(var0, b.b[8], var3_3, var2_2, 36);
                }
                if ((b.a & 1) == 0) break block15;
                v0 = var0;
                v1 = b.b;
                v2 = 9;
            }
            b.a(v0, v1[v2], var4_4, var2_2, 40);
        }
    }

    private static void a(boolean bl, boolean bl2) {
        block8: {
            Command command;
            Canvas canvas;
            block9: {
                block7: {
                    if (b != null) {
                        a.removeCommand(b);
                    }
                    if (a != null) {
                        a.removeCommand(a);
                    }
                    if (!d.a) break block7;
                    if (bl) {
                        a.addCommand(a);
                    }
                    if (!bl2) break block8;
                    canvas = a;
                    command = b;
                    break block9;
                }
                if (bl2) {
                    a.addCommand(b);
                }
                if (!bl) break block8;
                canvas = a;
                command = a;
            }
            canvas.addCommand(command);
        }
    }

    private static void e() {
        if (b != null) {
            a.removeCommand(b);
            b = null;
        }
        if (a != null) {
            a.removeCommand(a);
            a = null;
        }
    }

    private static void a(Graphics graphics, int n, int n2, int n3, int n4, int n5, int n6) {
        if (d.c) {
            int n7 = n5 >> 16;
            int n8 = n5 >> 8 & 0xFF;
            int n9 = n5 & 0xFF;
            int n10 = n6 >> 16;
            int n11 = n6 >> 8 & 0xFF;
            int n12 = n6 & 0xFF;
            if (n2 + n4 > al) {
                n4 = al - n2;
            }
            if (n + n3 > ak) {
                n3 = ak - n;
            }
            int n13 = n10 - n7;
            int n14 = n11 - n8;
            int n15 = n12 - n9;
            int n16 = n7;
            int n17 = n8;
            int n18 = n9;
            int n19 = 0;
            for (int i = n2; i < n2 + n4; ++i) {
                int n20;
                if (i < al / 2) {
                    n20 = i;
                } else if (i == al / 2) {
                    n16 = n10;
                    n17 = n11;
                    n18 = n12;
                    n20 = 0;
                } else {
                    n20 = al / 2 - i;
                }
                n19 = n20;
                graphics.setColor(n16 + n13 * n19 / (al / 2), n17 + n14 * n19 / (al / 2), n18 + n15 * n19 / (al / 2));
                graphics.drawLine(n, i, n + n3, i);
            }
        } else {
            graphics.setColor(n6);
            graphics.fillRect(n, n2, n3, n4);
        }
    }

    private static Image b(byte[] byArray, int n, int n2, int n3, int n4) {
        long l;
        int n5;
        int n6 = 0;
        for (int i = n; n6 == 0 && i < n + n2; ++i) {
            if ((byArray[i] & 0xFF) != 80 || (byArray[i + 1] & 0xFF) != 76 || (byArray[i + 2] & 0xFF) != 84 || (byArray[i + 3] & 0xFF) != 69) continue;
            n6 = i;
        }
        int n7 = (byArray[n6 - 4] << 24 & 0xFF000000) + (byArray[n6 - 3] << 16 & 0xFF0000) + (byArray[n6 - 2] << 8 & 0xFF00) + (byArray[n6 - 1] << 0 & 0xFF);
        byArray[n6 + 4 + 3 * n3] = (byte)((n4 & 0xFF0000) >> 16);
        byArray[n6 + 4 + 3 * n3 + 1] = (byte)((n4 & 0xFF00) >> 8);
        byArray[n6 + 4 + 3 * n3 + 2] = (byte)(n4 & 0xFF);
        byte[] byArray2 = new byte[n7 + 4];
        System.arraycopy((Object)byArray, (int)n6, (Object)byArray2, (int)0, (int)(n7 + 4));
        long[] lArray = new long[256];
        for (n5 = 0; n5 < 256; ++n5) {
            l = n5;
            for (int i = 0; i < 8; ++i) {
                l = (l & 1L) == 1L ? 0xEDB88320L ^ l >> 1 : l >> 1;
            }
            lArray[n5] = l;
        }
        l = 0xFFFFFFFFL;
        for (n5 = 0; n5 < byArray2.length; ++n5) {
            l = lArray[(int)(l ^ (long)byArray2[n5]) & 0xFF] ^ l >> 8;
        }
        byArray[n6 + 4 + n7] = (byte)(((l ^= 0xFFFFFFFFL) & 0xFFFFFFFFFF000000L) >> 24);
        byArray[n6 + 4 + n7 + 1] = (byte)((l & 0xFF0000L) >> 16);
        byArray[n6 + 4 + n7 + 2] = (byte)((l & 0xFF00L) >> 8);
        byArray[n6 + 4 + n7 + 3] = (byte)((l & 0xFFL) >> 0);
        System.gc();
        return b.a(byArray, n, n2);
    }

    private static void a(Graphics graphics, int n, int n2, int n3, int n4) {
        if (n3 > n4) {
            n3 = n4;
        }
        int n5 = (ak - n2) / 2;
        graphics.setColor(0xFFFFFF);
        graphics.drawRect(n5, n, n2, 6);
        int n6 = (n2 - 2 - 2) * n3 / n4 + 1;
        graphics.setColor(0xFF0000);
        graphics.fillRect(n5 + 1 + 1, n + 1 + 1, n6, 3);
    }

    private static void b(Graphics graphics, int n, int n2, int n3, int n4, int n5, int n6) {
        graphics.fillTriangle(n, n2, n3, n4, n5, n6);
    }

    private static void a(Graphics graphics, Image image, int n, int n2, int n3, int n4, int n5, int n6) {
        graphics.drawRegion(image, n, n2, n3, n4, 0, n5, n6, 20);
    }

    private static void a(Graphics graphics, Image image, int n, int n2, int n3) {
        int n4;
        int n5;
        int n6;
        Image image2;
        Graphics graphics2;
        if (d.l) {
            graphics2 = graphics;
            image2 = image;
            n6 = n;
            n5 = n2;
            n4 = n3;
        } else {
            if ((n3 & 1) != 0) {
                n -= image.getWidth() >> 1;
            }
            if ((n3 & 2) != 0) {
                n2 -= image.getHeight() >> 1;
            }
            if ((n3 & 8) != 0) {
                n -= image.getWidth();
            }
            if ((n3 & 0x20) != 0) {
                n2 -= image.getHeight();
            }
            graphics2 = graphics;
            image2 = image;
            n6 = n;
            n5 = n2;
            n4 = 0;
        }
        graphics2.drawImage(image2, n6, n5, n4);
    }

    private static void b(Graphics graphics, int n, int n2, int n3, int n4) {
        n = Math.max((int)n, (int)0);
        n2 = Math.max((int)n2, (int)0);
        n3 = Math.min((int)n3, (int)ak);
        n4 = Math.min((int)n4, (int)al);
        graphics.setClip(n, n2, n3, n4);
    }

    public final void run() {
        if (d.c == 2) {
            while (l) {
                try {
                    if (g != null) {
                        d = g;
                        b.g();
                        g = null;
                    }
                    Thread.sleep((long)1000L);
                }
                catch (Exception exception) {}
            }
        }
    }

    private static void f() {
        h = true;
        i = true;
        RecordStore recordStore = null;
        try {
            recordStore = RecordStore.openRecordStore((String)"igp19", (boolean)false);
        }
        catch (Exception exception) {
            try {
                recordStore = RecordStore.openRecordStore((String)"igp19", (boolean)true);
            }
            catch (Exception exception2) {}
        }
        try {
            if (recordStore != null) {
                recordStore.closeRecordStore();
            }
            return;
        }
        catch (Exception exception) {
            return;
        }
    }

    private static boolean c() {
        if (m) {
            if (i) {
                return h;
            }
            try {
                RecordStore recordStore = null;
                recordStore = RecordStore.openRecordStore((String)"igp19", (boolean)false);
                recordStore.closeRecordStore();
                h = true;
            }
            catch (Exception exception) {}
            i = true;
        }
        return h;
    }

    private static void g() {
        if (d != null && d.length() > 0) {
            String string = d;
            d = null;
            try {
                a.platformRequest(string);
                Thread.sleep((long)200L);
            }
            catch (Exception exception) {}
            int n = M = d.g ? 4 : 1;
            if (d.f) {
                a.notifyDestroyed();
            }
        }
    }

    public static boolean a(Graphics graphics, Image image, int n, int n2, int n3) {
        if (b.c()) {
            return false;
        }
        if (!b.a() || image == null || graphics == null) {
            return false;
        }
        if (System.currentTimeMillis() - a > 800L) {
            j = !j;
            a = System.currentTimeMillis();
        }
        if (j) {
            b.a(graphics, image, n, n2, n3);
            return true;
        }
        return true;
    }

    public final void commandAction(Command command, Displayable displayable) {
        if (k) {
            if (command == a) {
                b.a(25);
                return;
            }
            if (command == b) {
                b.a(26);
            }
        }
    }

    private static final void h() {
        a.put((Object)"URL-TEMPLATE-GAME", (Object)l);
        a.put((Object)"URL-OPERATOR", (Object)m);
        a.put((Object)"URL-PT", (Object)n);
        a.put((Object)"IGP-PROMOS", (Object)o);
        a.put((Object)"IGP-WN", (Object)p);
        a.put((Object)"IGP-BS", (Object)q);
        a.put((Object)"IGP-CATEGORIES", (Object)r);
        a.put((Object)"IGP-VERSION", (Object)s);
        a.put((Object)"URL-ORANGE", (Object)t);
        a.put((Object)"URL-GLIVE", (Object)u);
    }

    private static final String a(String string) {
        if (d.i) {
            String string2 = (String)a.get((Object)string);
            if (string2 != null && string2 != "") {
                return string2;
            }
            return null;
        }
        return a.getAppProperty(string);
    }

    static {
        a = 0xFF0000;
        b = d.a;
        v = -1;
        w = 14;
        A = 0;
        B = 1;
        C = 2;
        D = 3;
        b = new String[]{"URL-WN", "URL-BS", "URL"};
        a = new String[0];
        J = 6;
        K = 3;
        h = false;
        i = false;
        a = 0L;
        j = true;
        k = false;
        a = null;
        a = null;
        l = false;
        g = null;
        m = false;
        ac = -1;
        ao = 0;
        p = false;
        q = false;
        a = new Hashtable();
        l = "URL-TEMPLATE-GAME-XXX";
        m = "URL-OPERATOR-XXX";
        n = "URL-PT-XXX";
        o = "IGP-PROMOS-XXX";
        p = "IGP-WN-XXX";
        q = "IGP-BS-XXX";
        r = "IGP-CATEGORIES-XXX";
        s = "IGP-VERSION-XXX";
        t = "URL-ORANGE-XXX";
        u = "URL-GLIVE-XXX";
        ap = 0;
        a = false;
        b = false;
    }
}
