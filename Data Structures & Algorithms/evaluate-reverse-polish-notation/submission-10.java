class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int res = 0;
        for(String t : tokens){
            if (t.equals("+") || t.equals("-") || t.equals("*")|| t.equals("/")){
                int a = stack.pop();
                int b = stack.pop();
                if (t.equals("+")){
                    res = (a + b);
                    stack.push(res);
                }else if(t.equals("-")){
                    res = (b-a);
                    stack.push(res);
                }else if(t.equals("*")){
                    res = (a * b);
                    stack.push(res);
                }else{
                    res = (b / a);
                    stack.push(res);
                }

            }else{
                int number = Integer.parseInt(t);
                stack.push(number);
            }
        }
        return stack.peek();
    }
}
