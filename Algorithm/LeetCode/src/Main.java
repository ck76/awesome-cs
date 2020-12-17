import fanxing.A_Human;
import fanxing.Animal;
import fanxing.Human;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<? extends Human> list = new ArrayList<>();
//        list.add(new Human());
        list.add(new A_Human());
//        list.add(new Animal());

//        A_Human a_human=list.get(0);
        Human human= list.get(0);
        Animal animal=list.get(0);

        List<? super Human> list1 = new ArrayList<>();
        list1.add(new Human());
        list1.add(new A_Human());
        list1.add(new Animal());

        A_Human a_human1=list1.get(0);
        Human human1=list1.get(0);
        Animal animal1=list1.get(1);

    }
}

class Solution {

}
