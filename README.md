# 環境構築
```
$ docker run -itd --name kaggle -p 8886:8888 -e http_prox=yourProxy -e https_proxy=yourProxy -v path2pj:/notebooks kaggle/python
$ docker exec -it kaggle bash
$ jupyter notebook --notebook-dir=/notebooks --ip 0.0.0.0 --no-browser --allow-root --NotebookApp.token=password &
```

# jupyterExtension
```
$ docker exec -it kaggle bash
$ pip install jupyter_contrib_nbextensions
$ jupyter contrib nbextension install --user
$ jupyter nbextension enable codefolding/main
```

# KaggleCLIインストール(https://github.com/Kaggle/kaggle-api)
```
$ pip install kaggle
```

# APIトークン発行
- www.kaggle.com -> Your Account -> Create New API token
- kaggle.jsonをダウンロード
- kaggle.jsonをコンテナにコピー

```
$ mv kaggle.json ~/.kaggle/
$ chmod 600 ~/.kaggle/kaggle.json
```

# Proxy設定
```
kaggle config set -n proxy -v yourProxy
```
