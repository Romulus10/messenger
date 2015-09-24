package jmessage;

import java.io.IOException;

public class JMessage {

    static int key;

    public static void main(String[] args) throws IOException {
        Resources.list.start();
        Resources.send.run();
    }
}
