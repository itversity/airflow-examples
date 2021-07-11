DATA_DIR=${1}
FILE_HOUR=${2}
echo "Downloading the file for ${FILE_HOUR}"
cd ${DATA_DIR} && curl -O https://data.gharchive.org/${FILE_HOUR}.json.gz
