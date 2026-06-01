class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
    
        # FIX: Creating arrays of 26 zeros correctly without a loose starred expression
        s1_count = [0 for _ in range(26)]
        s2_count = [0 for _ in range(26)]
        
        # Fill counts for s1 and the very first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # 2. Compute initial match count
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        # print("--- SETUP ---")
        # print(f"s1: '{s1}'")
        # print(f"Initial Window in s2: '{s2[:len(s1)]}'")
        # print(f"Starting Matches: {matches}/26")
        # print("-" * 30)
        
        # If the first window is already a perfect match
        if matches == 26:
            # print("Success on the first try!")
            return True
            
        # 3. Slide the window
        left = 0
        for right in range(len(s1), len(s2)):
            # print(f"\n--- Sliding Window: Move right to index {right} ('{s2[right]}') ---")
            # print(f"Current window before slide: '{s2[left:right]}'")
            
            # --- HANDLE RIGHT CHARACTER (INCOMING) ---
            r_idx = ord(s2[right]) - ord('a')
            s2_count[r_idx] += 1
            
            if s2_count[r_idx] == s1_count[r_idx]:
                matches += 1
                # print(f"  -> Added '{s2[right]}': Character count now MATCHES s1! Matches +1 ({matches})")
            elif s2_count[r_idx] == s1_count[r_idx] + 1:
                matches -= 1
                # print(f"  -> Added '{s2[right]}': Too many '{s2[right]}'s now! Matches -1 ({matches})")
            else:
                print(f"  -> Added '{s2[right]}': No change to match status ({matches})")
                
            # --- HANDLE LEFT CHARACTER (OUTGOING) ---
            l_idx = ord(s2[left]) - ord('a')
            s2_count[l_idx] -= 1
            
            if s2_count[l_idx] == s1_count[l_idx]:
                matches += 1
                # print(f"  -> Removed '{s2[left]}': Character count now MATCHES s1! Matches +1 ({matches})")
            elif s2_count[l_idx] == s1_count[l_idx] - 1:
                matches -= 1
                # print(f"  -> Removed '{s2[left]}': Lost a required '{s2[left]}'! Matches -1 ({matches})")
            else:
                print(f"  -> Removed '{s2[left]}': No change to match status ({matches})")
                
            # Move the left boundary of the window forward
            left += 1
            print(f"New window frame: '{s2[left:right+1]}'")
            
            # Check if we hit the jackpot
            if matches == 26:
                print(f"\nSUCCESS! Found a permutation at window '{s2[left:right+1]}'")
                return True
                
        # print("\nFINISHED: No permutation found.")
        return False