public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        List<Integer> result = new ArrayList<Integer>();
        combinationHelper(candidates,0, target, results, result);
        return results;
    }
    private void combinationHelper(int[] candidates,int index, int target, List<List<Integer>> results, List<Integer> result) {
        if(target < 0) return;
        if(target == 0) {
            results.add(new ArrayList<Integer>(result));
            return;
        }
        for(int i = index; i< candidates.length; i++) { 
            result.add(candidates[i]);
            combinationHelper(candidates, i, target-candidates[i], results, result);// [index]
            result.remove(result.size()-1);
        }
    }
}
