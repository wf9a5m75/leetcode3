# 002. プログラミング初心者が書いたコードのレビュー (TypeScript)

<details>
  <summary>問題の設定</summary>

- PythonとTypeScriptでは、コードに対する文化に多少の違いがあるので、TypeScriptだけを考慮した問題を生成してもらうことにした。
- プログラミング初心者がLeetCode easyの問題を解いたコードを想定生成してもらう。
- 可読性の良くないコードにしてもらう
</details>

<details open>
  <summary>問題：Palindrome Number</summary>

## 問題説明

与えられた整数が回文であるかどうかを判断します。整数が回文である場合は`true`を返し、そうでない場合は`false`を返します。

例えば、`121`は回文ですが、`-121`や`10`は回文ではありません。


### TypeScriptの解法コード（バグ含む、可読性が低い）
```typescript
function isPalindrome(x: number): boolean {
    if (x < 0) return false;
    let str = x.toString();
    let rev = "";
    for (let i = 0; i < str.length; i++) {
        rev = str[i] + rev;
    }
    return rev == str;
}

console.log(isPalindrome(121)); // true
console.log(isPalindrome(-121)); // false
console.log(isPalindrome(10)); // false
console.log(isPalindrome(1221)); // true
```
コードをレビューして、どのような問題点があるかを教えてください。その後、フィードバックを行います。
</details>


<details>
  <summary>勝又レビュー</summary>

1. コードの可読性:
  - 1文字変数名は、慣例的にループで使用される `i`や`j`を除けば、使用するのは避けるほうが、コードの可読性があがります。
  また変数`rev`は`reversed`を頭文字だと推測しますが、`reversedX` のように意味合いが伝わる変数名が良いと思います。

  - ifの後ろには改行を入れると、コードの可読性が向上しますよ。
  ```typescript
  if (num < 0) {
      return false;
  }
  ```

  - `xString`は変化しないので、`let`ではなく`const`を使いましょう。コードの読み手に、この変数は変化しない、ということを明示的に示すことができます。
  - 今回のコードでは不具合を起こすことはありませんが、JavaScrip/TypeScriptでの等価比較は`==`のかわりに`===`を使用するほうが良いです。`===`は変数型が同じかどうかをチェックします。

  - 具体的には以下のようにするのはどうでしょうか。
  ```typescript
  function isPalindrome(num: number): boolean {
      if (num < 0) {
        return false;
      }
      const xString = num.toString();
      let reversedX = "";
      for (let i = 0; i < xString.length; i++) {
          reversedX = xString[i] + reversedX;
      }
      return reversedX === xString;
  }
  ```

2. パフォーマンス:
  - `for`ループ内で`reversedX = xString[i] + reversedX;` としていますが、`reversedX`に`reversedX.length + 1`のメモリ空間をループするたびに作成・コピーすることになります。
    つまり`O(N^2)`の時間計算量になります。
    短い文字列ではパフォーマンスに大きな問題はないですが、長い文字列になると影響が出てきます。

  - 文字列を反転させるだけなら、`const reversedX = xString.split().toReversed().join('');` とするのはどうでしょうか。`O(N)`の時間計算量で反転した文字列を作成できます。
  
  - 具体的には以下のようになります。コード全体がシンプルになり、可読性とパフォーマンスが向上します。
  ```typescript
  function isPalindrome(num: number): boolean {
      if (num < 0) {
        return false;
      }
      const xString = num.toString();
      const reversedX = xString.split().toReversed().join('');
      return reversedX === xString;
  }
  ```

3. セキュリティ:
 - `isPalindrome()`の引数`x`についてです。
  「整数が与えられる」ことが問題文で示されているので、ここまで考慮しなくても良いかもしれませんが、`x`が整数かどうかをチェックするのが良いと思います。
  具体的には次のように行います。

  ```typescript
  function isPalindrome(x: number): boolean {
      if (!Number.isInteger(x)) {
          throw new TypeError('The x must be an integer value');
      }
      if (x < 0) {
          return false;
      }
      const xString = num.toString();
      const reversedX = xString.split().toReversed().join('');
      return reversedX === xString;
  }
  ```

4. コメント:
  - アルゴリズムのロジックを簡単にコメントしておくと、読み手に取ってコードを理解しやすくなります。
  - 具体的には以下のようなコメントです。
  - 
  ```typescript
  /**
   * Returns true if the given an integer x is palindromic.
   *
   * @params {number} x - An integer number.
   * @returns {boolean} - Whether the x is palindromic or not.
   */
  function isPalindrome(x: number): boolean {
      // Throws an error if x is not an integer for just in case.
      if (!Number.isInteger(x)) {
          throw new TypeError('The x must be an integer value');
      }
      // A negative value can not be palindromic.
      if (x < 0) {
          return false;
      }

      // Makes a reversed string of X, then compares both strings.
      const xString = num.toString();
      const reversedX = xString.split().toReversed().join('');
      return reversedX === xString;
  }
  ```
</details>
