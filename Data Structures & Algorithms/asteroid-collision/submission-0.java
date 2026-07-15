class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();
    for (int a : asteroids) {
        boolean alive = true;
        while (alive && a < 0 && !stack.isEmpty() && stack.peek() > 0) {
            if (stack.peek() < -a) {
                stack.pop();          // top explodes, keep checking
            } else if (stack.peek() == -a) {
                stack.pop();          // both explode
                alive = false;
            } else {
                alive = false;        // incoming explodes
            }
        }
        if (alive) stack.push(a);
    }
    int[] res = new int[stack.size()];
    for (int i = res.length - 1; i >= 0; i--) res[i] = stack.pop();
    return res;
    }
}