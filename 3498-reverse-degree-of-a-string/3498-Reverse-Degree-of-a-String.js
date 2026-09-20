/**
 * @param {string} s
 * @return {number}
 */
var reverseDegree = function(s) {
    let st=s.split('')
    let arp = st.map((ch,i) => (i+1)*(26-("abcdefghijklmnopqrstuvwxyz".split('').indexOf(ch))));
    return arp.reduce((su,n)=>su+n,0)
};