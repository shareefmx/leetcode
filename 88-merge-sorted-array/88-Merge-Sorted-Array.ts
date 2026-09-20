/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
    let arr:number[]=[...nums1.slice(0,m),...nums2.slice(0,n)].sort((a,b)=>a-b)
    console.log(arr)
   for (let i: number = 0; i < arr.length; i++) {
        nums1[i] = arr[i];
    }
};