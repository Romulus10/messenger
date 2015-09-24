package jmessage;

public class Encrypter {

    int key;

    public Encrypter(int key) {
        this.key = key;
    }

    public String encode(String message) {
        String end = "";
        String[] x = message.split("");
        //Get the ASCII value of each character in the array, then
        //apply the encoder key. 
        //Then change that number into a string and send it.
        /*
         for(int i = 0; i < x.length; i++)
         {
         x[i] = Integer.toString(((int)(x[i].charAt(0)))+key);
         }
         */
        for (int i = 0; i < x.length; i++) {
            end = end + x[i];
        }
        return end;
    }

    public String decode(String message) {
        String end = "";
        String[] x = message.split("");
        /*
         for(int i = 0; i < x.length; i++)
         {
         x[i] = Character.toString((char)(((int)(x[i].charAt(0)))-key));
         }
         */
        for (int i = 0; i < x.length; i++) {
            end = end + x[i];
        }
        return end;
    }
}
