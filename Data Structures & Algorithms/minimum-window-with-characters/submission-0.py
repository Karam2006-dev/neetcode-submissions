from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        i = I = J = 0
        
        # j: sağ işaretçi (pencere bitişi, 1-based indexing için enumerate 1'den başlar)
        # c: sağ işaretçideki karakter
        for j, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            
            # Aradığımız tüm karakterleri içeren geçerli bir pencere bulduk mu?
            if missing == 0:
                # Soldan gereksiz (fazladan alınmış veya t'de hiç olmayan) karakterleri atıp pencereyi daralt
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                
                # Mevcut pencere şimdiye kadarki en kısasıysa kaydet
                if not J or j - i <= J - I:
                    I, J = i, j
                    
        return s[I:J]