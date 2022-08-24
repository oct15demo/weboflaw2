echo ""
echo "blank types are files without extensions"
echo ""
echo "count file extension      type"
ls|xargs file {}  |awk -F'.' '{print $2;}'|grep -v ^"sh: "|sed 's/ [ ]*/	/'|sort|uniq -c


echo ""
echo "with and without very long lines combined"
echo ""
echo "count file extension      type"
ls|xargs file {}  |awk -F'.' '{print $2;}'|sed 's/, with very long lines//'|grep -v ^"sh: "|sed 's/ [ ]*/	/'|sort|uniq -c

echo ""
echo "empty files"
for file in `ls`
do
   output=`file $file|awk '{print $2}'|grep empty`
   if [ "" != "$output" ]
   then
      file $file
   fi
done

echo ""
echo "gzip files"
for file in `ls`
do
   output=`file $file|awk '{print $2}'|grep gzip`
   if [ "" != "$output" ]
   then
      file $file
   fi
done
echo ""
