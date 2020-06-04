# 811. Subdomain Visit Count
# hash table


#  using defaultdict() method to solve
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.defaultdict(int)
        for domain in cpdomains:
            count, d = domain.split()
            count = int(count)
            frags = d.split('.')
            for i in range(len(frags)):
                ans['.'.join(frags[i:])] += count
        return ['{} {}'.format(c, d) for d, c in ans.items()]