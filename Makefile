# -*- coding: utf-8 -*-
#
FNAME=ldcc-20140209.tar.gz
MECAB_OPTS = -b 40000
FINAL_OUTPUTS = train-abstract.txt train-article.txt \
	test-abstract.txt test-article.txt

# download
$(FNAME):
	wget https://www.rondhuit.com/download/$(FNAME)
# unpack
text: $(FNAME)
	tar xvf $(FNAME)

# make article/abstract pair
abstract.txt article.txt: text
	python make_pair.py

# normalize
pp-abstract.txt pp-article.txt: abstract.txt article.txt
	python preprocess.py

# word segmentation
# TODO: take care about too longer lines
wakati-pp-abstract.txt wakati-pp-article.txt: pp-abstract.txt pp-article.txt
	mecab -Owakati $(MECAB_OPTS) < pp-abstract.txt > wakati-pp-abstract.txt
	mecab -Owakati $(MECAB_OPTS) < pp-article.txt > wakati-pp-article.txt

# shuffle and split
$(FINAL_OUTPUTS): wakati-pp-abstract.txt wakati-pp-article.txt
	python split.py

all: $(FINAL_OUTPUTS)

#
clean:
	-rm -rf text
	rm -f abstract.txt article.txt
	rm -f pp-abstract.txt pp-article.txt
	rm -f wakati-pp-abstract.txt wakati-pp-article.txt
	rm -f $(FINAL_OUTPUTS)
