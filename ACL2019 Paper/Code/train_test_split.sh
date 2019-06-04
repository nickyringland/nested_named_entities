#############################################
#   section 02 as development set
#   section 23-24 as test set
#   the remaining sections as training set
#############################################

FROM=../Resources/with-text
TO=../Resources/split

mkdir $TO

for i in 00 01 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22
do
    echo "move section $i to train set"
    cat $FROM/$i/* >> $TO/train.txt
done

for i in 02
do
    echo "move section $i to development set"
    cat $FROM/$i/* >> $TO/dev.txt
done

for i in 23 24
do
    echo "move section $i to test set"
    cat $FROM/$i/* >> $TO/test.txt
done