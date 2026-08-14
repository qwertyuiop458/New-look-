/*
 * Decompiled with CFR 0.152.
 * 
 * Could not load the following classes:
 *  java.lang.Exception
 *  java.lang.Object
 *  java.lang.String
 *  java.lang.System
 *  javax.microedition.io.Connector
 *  javax.microedition.sensor.ChannelInfo
 *  javax.microedition.sensor.Data
 *  javax.microedition.sensor.DataListener
 *  javax.microedition.sensor.SensorConnection
 *  javax.microedition.sensor.SensorInfo
 *  javax.microedition.sensor.SensorManager
 */
import javax.microedition.io.Connector;
import javax.microedition.sensor.ChannelInfo;
import javax.microedition.sensor.Data;
import javax.microedition.sensor.DataListener;
import javax.microedition.sensor.SensorConnection;
import javax.microedition.sensor.SensorInfo;
import javax.microedition.sensor.SensorManager;

/*
 * Duplicate member names - consider using --renamedupmembers true
 */
public final class e
implements DataListener {
    public static boolean a = true;
    public int[] a;
    public String[] a;
    public boolean b;
    public String a;
    public SensorConnection a;
    public boolean c = false;
    public int a = new String[3];
    public int b;
    public int[] b = new int[]{0, 0, 0};
    public static int c;
    public static int d;

    public final void a() {
        String string = System.getProperty((String)"microedition.sensor.version");
        if (string == null) {
            this.b = false;
            return;
        }
        this.b = true;
        try {
            SensorInfo[] sensorInfoArray = SensorManager.findSensors((String)"acceleration", (String)SensorInfo.CONTEXT_TYPE_USER);
            for (int i = 0; i < sensorInfoArray.length; ++i) {
                SensorInfo sensorInfo = sensorInfoArray[i];
                this.a = sensorInfo.getUrl();
                ChannelInfo[] channelInfoArray = sensorInfo.getChannelInfos();
                for (int j = 0; j < channelInfoArray.length; ++j) {
                    this.a[j] = channelInfoArray[j].getName();
                }
            }
            this.a = (SensorConnection)Connector.open((String)this.a);
            this.a.setDataListener((DataListener)this, 1);
            return;
        }
        catch (Exception exception) {
            return;
        }
    }

    public static boolean a() {
        return true;
    }

    public static boolean b() {
        return a;
    }

    public static void a(boolean bl) {
        a = bl;
        g.c();
    }

    public final void dataReceived(SensorConnection sensorConnection, Data[] dataArray, boolean bl) {
        block7: {
            if (!this.b) break block7;
            try {
                block10: {
                    block9: {
                        block8: {
                            for (int i = 0; i < dataArray.length; ++i) {
                                int n;
                                int[] nArray;
                                if (dataArray[i].getChannelInfo().getName().compareTo(this.a[0]) == 0) {
                                    nArray = this.a;
                                    n = 0;
                                } else if (dataArray[i].getChannelInfo().getName().compareTo(this.a[1]) == 0) {
                                    nArray = this.a;
                                    n = 1;
                                } else {
                                    nArray = this.a;
                                    n = 2;
                                }
                                nArray[n] = dataArray[i].getIntValues()[0] / 10;
                            }
                            if (!this.c) break block8;
                            if (this.a++ <= this.b) break block9;
                            break block10;
                        }
                        this.b();
                        this.b[0] = this.a[0];
                        this.b[1] = this.a[1];
                        this.b[2] = this.a[2];
                    }
                    return;
                }
                this.c = false;
            }
            catch (Exception exception) {}
        }
    }

    private void b() {
        if (this.a[0] >= 0 && this.b[0] < 0) {
            ++c;
            d = 0;
            return;
        }
        if (this.a[0] < 0 && this.b[0] >= 0) {
            ++c;
            d = 0;
            return;
        }
        if (this.a[1] >= 0 && this.b[1] < 0) {
            ++c;
            d = 0;
            return;
        }
        if (this.a[1] < 0 && this.b[1] >= 0) {
            ++c;
            d = 0;
            return;
        }
        if (c > 0 && ++d > 3) {
            c = 0;
        }
    }

    public static boolean c() {
        if (!a) {
            return false;
        }
        if (c > 4) {
            c = 0;
            d = 0;
            return true;
        }
        return false;
    }
}
