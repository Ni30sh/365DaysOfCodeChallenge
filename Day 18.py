def compute_lps_array(pat):
    M = len(pat)
    lps = [0] * M
    length = 0
    i = 1

    while i < M:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(txt, pat):
    N = len(txt)
    M = len(pat)
    lps = compute_lps_array(pat)
    result = []

    i = 0  # index for txt
    j = 0  # index for pat

    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            result.append(i - j)
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result

# Example usage
txt1 = "abcab"
pat1 = "ab"
print(kmp_search(txt1, pat1))  # Output: [0, 3]

txt2 = "abesdu"
pat2 = "edu"
print(kmp_search(txt2, pat2))  # Output: []

txt3 = "aabaacaadaabaaba"
pat3 = "aaba"
print(kmp_search(txt3, pat3))  # Output: [0, 9, 12]