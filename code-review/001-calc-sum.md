# 001. 簡単なレビュー (Python3)

<details>
  <summary>背景</summary>

- コードレビューについて理解をするため、簡単なコードに対してコードレビューを行い、それについてフィードバックをしていただきたいです。
- 例えば、「このレビューはこういう点をもっと指摘する方が良い」とか「このレビューはなくても良さそう」など。
- 私の基軸言語がTypeScriptなので、Pythonの文化については、そこまで詳しくないです。
</details>
<details>
  <summary>問題文</summary>

## 問題：以下のコードについて、コードレビューを行ってください。

```python
def calc_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

def main():
    numbers = [1, 2, 3, 4, 5]
    print("Sum:", calc_sum(numbers))

if __name__ == "__main__":
    main()
```

以下にレビューのテンプレートを用意しましたので、これに従ってコメントしてください。

1. コードの可読性:
2. コードの正確性:
3. パフォーマンス:
4. セキュリティ:
5. コーディング規約の遵守:
6. メンテナンス性:
7. その他のコメント:
</details>

<details open>
  <summary>勝又のコードレビュー</summary>

## 1. コードの可読性:

- プログラムのエントリーポイントが `main()`というのは、どこからコードを読めばよいか分かりやすく良いと思います。
- numbers という変数名は、数字が複数入っている、ということが分かるので良いですね。
- typingモジュールを使用して、変数形を示してもらえると、コードの可読性が向上します。
例えば以下のとおりです。

```python
from typing import List

def calc_sum(numbers: List[int]) -> int:
```

## 2. コードの正確性:

- `calc_sum(numbers)` という関数名から、`calc_sums()`は `numbers`の中に入っている数字の合計を返すものと推測します。
このコードにおいては、正しく実装できていると思います。

## 3. パフォーマンス:

- このコードでは、for文でループするために、`range(len(numbers))` を用いています。
- `for num in numbers`とすると、`range`を使って新しいイテレーションを生成する必要がなく、シンプルに書けますよ。

## 4. セキュリティ:

- 変数型が指定されていないので、`calc_sum(numbers)` の `numbers`に何が含まれてくるのか分からないです。
- 少し過剰かもしれませんが、セキュリティの面においては、配列の内容が数値かどうかを判定したほうが良いかもしれません。
例えば以下のとおりです。

```python
def calc_sum(numbers):
   total = 0
   for i in range(len(numbers)):
       kind = type(numbers[i])
       if isinstance(kind, int) or isinstance(kind, float):
           total += numbers[i]
   return total
```

## 5. コーディング規約の遵守:

- プログラムの全体が lower_snake_case で統一されていて良いと思います。

## 6. メンテナンス性:

- メンテナンス性の面から考えると、標準関数`sum()`で `calc_sum()`を置換することが出来そうです。

## 7. その他のコメント:

- 全体として大きな問題点は有りません。良いと思います。
</details>
