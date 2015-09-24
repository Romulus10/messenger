package jmessage;

public class Encrypter {

    int key;

    public Encrypter(int key) {
        this.key = key;
    }

    public String encode(String message) {
        String end = "";
        String[] x = message.split("");
        for (int i = 0; i < x.length; i++) {
            char letter = x[i].charAt(0);
            int value = (int) letter;
            value = (((value * this.key) + this.key) / this.key);
            x[i] = Integer.toString(value);
        }
        for (int i = 0; i < x.length; i++) {
            end = end + (x[i] + " ");
        }
        return end;
    }
    
    public String decode(String message) {
        String end = "";
        String[] x = message.split(" ");
        for (int i = 0; i < x.length; i++) {
            int first = Integer.valueOf(x[i]);
            first = (((first * this.key) - this.key) / this.key);
            char second = (char)first;
            x[i] = Character.toString(second);
        }
        for (int i = 0; i < x.length; i++) {
            end = end + x[i];
        }
        return end;
    }
}
