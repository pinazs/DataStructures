/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Pinaz
 */
public class Max_3 {
     public int thirdMax(int[] nums) {
          Integer max = null;
          Integer second_max = null;
          Integer third_max = null;
        
              for (Integer val : nums)
              {
                 
                  if (val.equals(max) || val.equals(second_max) || val.equals(third_max) )
                  {
                      //System.out.println("First if");
                      continue;
                  }
                  if(max == null || val >  max)
                  {
                     // System.out.println("Second if");
                      third_max= second_max;
                      second_max=max;
                      max=val;
                  }
                  else if (second_max == null || val > second_max)
                  {
                      //System.out.println("Third if");
                      third_max= second_max;
                      second_max = val;
                  }
                  else if (third_max == null || val > third_max)
                  {
                      //System.out.println("fourth if");
                      third_max = val;
                  }
                   
              }
     
        if(third_max == null)
        {
            return max;
        }
        return third_max;
    }

    public static void main(String[] arg)
    {
        Max_3 mn= new Max_3();
        int[] a1 = new int[]{3,2,4,8,2,3,9};
        int max_three = mn.thirdMax(a1);
        System.out.println("Third Max: "+max_three);
    }
}
