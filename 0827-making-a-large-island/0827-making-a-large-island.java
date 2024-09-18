class Solution {
    int[][] moves = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int largestIsland(int[][] grid) {
        Map<Integer, Integer> areaMap = new HashMap<>();
        int mark = 2;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    int area = getArea(grid, i, j, mark);
                    areaMap.put(mark++, area);
                }
            }
        }

        int maxArea = Integer.MIN_VALUE;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 0) {
                    int currArea = 1;
                    Set<Integer> set = new HashSet<>();
                    for (int[] move: moves) {
                    int currI = i + move[0];
                    int currJ = j + move[1];
                    if (currI >= 0 && currI < grid.length && currJ >= 0 && currJ < grid[0].length 
                        && grid[currI][currJ] != 0 && !set.contains(grid[currI][currJ])) {
                        currArea += areaMap.get(grid[currI][currJ]);
                        set.add(grid[currI][currJ]);
                        }
                    }
                    maxArea = Math.max(currArea, maxArea);
                }
            }
        }

        return maxArea == Integer.MIN_VALUE ? grid.length * grid[0].length : maxArea;
    }

    private int getArea(int[][] grid, int i, int j, int mark) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || grid[i][j] != 1) {
            return 0;
        }

        grid[i][j] = mark;
        return 1 + getArea(grid, i - 1, j, mark) + getArea(grid, i + 1, j, mark) + getArea(grid, i, j - 1, mark) + getArea(grid, i, j + 1, mark);
    }
}