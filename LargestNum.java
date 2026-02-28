import java.util.*;
public class LargestNum {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        List<Integer> arr = new ArrayList<>();
        StringBuilder number = new StringBuilder();
        for(char ch : line.toCharArray()){
            if(Character.isDigit(ch)){
                number.append(ch);
            }else{
                if(number.length() > 0){
                    arr.add(Integer.parseInt(number.toString()));
                    number.setLength(0);
                }
            }
        }
        if(number.length() > 0){
            arr.add(Integer.parseInt(number.toString()));
        }
        int max = Integer.MIN_VALUE;
        for(int ar : arr){
            if(max < ar) max = ar;
        }
        System.out.println("Maximum elemt in array is: "+ max);
        }
    }
