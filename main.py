from datetime import datetime
from functions import get_datalayer, get_sitemap, check_datalayer_object
from send_mail import send_mail

dl_values = ['page_type', 'page_id', 'environment']
receivers = [] # add list of mail-receivers
sitemap_url = "https://www.amazon.com/sitemap.xml" # add your sitemap URL
date = datetime.now()
date_str = date.strftime('%Y-%m-%d')

def run_qa(url, dl_values):
    data = []
    sitemap = get_sitemap(url, limit = 10)
    for url in sitemap:
        dl = get_datalayer(url, index = 0)
        missing_values = check_datalayer_object(dl, dl_values)
        result = {}
        result['url'] = url
        result['missing_values'] = missing_values
        data.append(result)
        result['date'] = date_str
        result['qa_values'] = dl_values
    df = pd.DataFrame.from_records(data)
    df[df['missing_values'].apply(lambda x: len(x)) > 0]
    df.to_csv('file.csv', sep=',', encoding='utf-8')
    send_mail(receivers ,"Test CMS datalayer QA", 'file.csv', 'filename.csv')

run_qa(sitemap_url, dl_values)
