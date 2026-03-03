import java.util.*;
public class ReverseArray {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        List<Integer> arr = new ArrayList<>();
        StringBuilder num = new StringBuilder();
        for(char ch : line.toCharArray()){
            if(Character.isDigit(ch)){
                num.append(ch);
            }else{
                if(num.length() > 0){
                    arr.add(Integer.parseInt(num.toString()));
                    num.setLength(0);
                }
            }
        }
        if(num.length() > 0){
            arr.add(Integer.parseInt(num.toString()));
        }
            /// Reversing an Array using two - pointers
        // int i = 0;
        // int j = arr.size() - 1;
        // while(i < j){
        //     int temp = arr.get(i);
        //      arr.set(i,arr.get(j));
        //     arr.set(j,temp);
        //     i++;
        //     j--;
        // }
        // System.out.println(arr);
        //-----------------------------------------------------------------------
        int sum = 0;
        for(int ar : arr){
            sum += ar;
        }
        System.out.println("Sum of elemnts in array are :" + sum);

    }
    
}
