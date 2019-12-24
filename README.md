# Atcoder  
atcoderのソースコードと用いたアルゴリズムをまとめる
## 組み合わせ問題
集合に対して任意の組み合わせを求める0か1を割り当てていく問題。

### 全探索  
基本的にはこの問題が多い。 for文を任意個数もちいて任意の長さの組み合わせを列挙する。 うまく時間計算量を減らす工夫が必要なことが多い  
- https://atcoder.jp/contests/abc145/tasks/abc145_c
- https://atcoder.jp/contests/abc085/tasks/abc085_c
- https://atcoder.jp/contests/abc051/tasks/abc051_b

### bit全探索
2進数を1bitずつ加算or減算しながらfor文を回し、1が立っている部分を配列から取り出すことで、配列の要素のすべての組み合わせを列挙することができる。  
- https://atcoder.jp/contests/abc147/tasks/abc147_c

### 二分探索
ソート済みの集合に対して任意の数を高速に探索することができる。pythonではライブラリが用意されているので用いるとよい。
- https://atcoder.jp/contests/abc143/tasks/abc143_d


### 貪欲法
組み合わせ問題(0か1に分ける問題）においてその時の最善の選択肢（局所解）をとっていく手法。計算量がO(N)で済む。
- https://atcoder.jp/contests/abc148/tasks/abc148_d


## 部分和問題（動的計画法）
集合Aの数字を組み合わせることでNと同じ値になるか求める問題。Nの長さの配列を用意し、for文で1ずつ見ていく。 現在の位置から集合Aの数字分引いた要素が先頭の要素、もしくは1ならば現在の要素に１をそうでないなら0を書き込んでいき、N番目の要素が1かを調べる。  
- https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c

## しゃくとり法
配列上の隣接している要素における任意の長さの集合を求めるためのアルゴリズム。2つの変数を用意し、その2つの変数を尺取り虫のように動かしていく。  
外側のfor文で頭の変数を加算していき。尻尾から頭の配列が条件を超えたら内側のfor文で尻尾を動かす。条件内に戻ったら次のループに移り再度頭を動かしていく。  
- https://atcoder.jp/contests/abc051/tasks/abc051_b
