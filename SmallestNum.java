import java.util.*;
public class SmallestNum {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            // int n = sc.nextInt();
            // int[] arr = new int[n];
            // for(int i = 0 ; i < n ; i++){                              // when size of arr is given
            //     arr[i] = sc.nextInt();
            // }
            // int min = Integer.MAX_VALUE;
            // for(int num : arr){
            //     if(num < min) min = num;
            // }
            // System.out.println("the Smallest elemnet in array is :" + min);
            //---------------------------------------------------------------------------------------------------------------------------
            // String line = sc.nextLine();
            // String[] tokens = line.split("\\s+");
            // List<Integer> arr = new ArrayList<>();
            // for(String token : tokens){                                      //when  arr  size is not given
            //     arr.add(Integer.parseInt(token));
            // }
            // int min = Integer.MAX_VALUE;
            // for(int num : arr){
            //     if(num < min) min = num;
            // }
            // System.out.println("Smallest number in arr is :" + min);
            //---------------------------------------------------------------------------------------------------------------------------------
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
            int min = Integer.MAX_VALUE;
            for(int ar : arr){
                if(ar < min) min = ar;
            }
            System.out.println("smallest num is : " + min);


    }
    
}
