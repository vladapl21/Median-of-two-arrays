class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
      """
      :type nums1: List[int]
      :type nums2: List[int]
      :rtype: float
      """
      merge = []
      while nums1 != [] or nums2 != []:
          if nums1 == []:
              merge.append(nums2[0])
              nums2.pop(0)
          elif nums2 == []:
              merge.append(nums1[0])
              nums1.pop(0)
          elif nums1[0] < nums2[0]:
              merge.append(nums1[0])
              nums1.pop(0)
          elif nums2[0] < nums1[0]:
              merge.append(nums2[0])
              nums2.pop(0)
          else:
              merge.append(nums1[0])
              nums1.pop(0)

      while len(merge) > 2:
          merge = merge[1:-1]
      if len(merge) == 1:
          return merge[0]
      else:
          return float(float(float(merge[0]) + float(merge[1]))/2)