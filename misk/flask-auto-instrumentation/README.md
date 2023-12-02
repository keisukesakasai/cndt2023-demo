## Automatic instrumentation と Programmatic instrumentation
- それぞれ、Instrumentor を完全自動で起動するか、コード内で起動するかの違い
- Automatic Instrumentation はコードに手を入れる必要がない。完全自動計装
- Programmatic Instrumentation はコード内でトレーサーやらメーターやらを起動する必要がある
  - ただ、Instrumentor() 起動時に設定できるオプションなどを使うことができる
  - たとえば、request_hook や response_hook などはその例（Flask, Django, FastAPI, Redis...e.t.c）
    - これを使うことで、Span に Attribute を差し込めたりする

一長一短だよなぁ。
まずサクッと始めたいなら自動計装して、使ってるうちに要望が出たら、コード内...が理想線なのかな。完全自動計装しちゃったらもうアプリ軽装するのめんどくさくなりそうな一方で、利便性がちゃんと理解されれば、別の箇所もやるためにコードに計装しようってなるのかもしれない...

特に、メトリクスなんかは、アプリケーションの中のロジックを使ってカスタムメトリクス生成などは旨みあるよね。
トレーシングもカスタムラベルの付与はやりたいかなぁ。。。

## 留意
- auto-isntrument してなお programamtic instrument するとすでに計装済みということで programmatic の方はスキップされる
- フツーにやると、tracer が 2 つ設定されてしまうから、global 変数から持ってくるようにする必要がある