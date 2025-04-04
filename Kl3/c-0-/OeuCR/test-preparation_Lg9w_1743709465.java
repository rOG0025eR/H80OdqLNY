int ans=0;
	        int small =0;
	        for(int i=0;i<j;i++) {
	            if(nums[i]<nums[j]) small++;
	        }
	        
	        int large =0;
	        for(int k=j+1;k<nums.length;k++) {
	            if(nums[j]<nums[k]) large++;
	        }
	        ans+=(small*large);
	    }
	    return ans;
