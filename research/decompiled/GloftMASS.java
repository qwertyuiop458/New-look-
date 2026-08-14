/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  java.lang.Object
 *  javax.microedition.lcdui.Display
 *  javax.microedition.midlet.MIDlet
 */
import javax.microedition.lcdui.Display;
import javax.microedition.midlet.MIDlet;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public class GloftMASS
extends MIDlet {
    public static g a;
    public static GloftMASS a;

    public GloftMASS() {
        a = this;
        Display.getDisplay((MIDlet)this);
        a = new g();
    }

    public void startApp() {
        a.l();
    }

    public void pauseApp() {
        g.k();
    }

    public void destroyApp(boolean bl) {
        a = null;
        this.notifyDestroyed();
    }
}
