from typing import Dict, Optional

class TDocument:
    def __init__(self, url: str, pub_date: int, fetch_time: int, text: str):
        self.url = url
        self.pub_date = pub_date
        self.fetch_time = fetch_time
        self.text = text
        self.first_fetch_time = fetch_time

    def __repr__(self):
        return (f"TDocument(url={self.url}, pub_date={self.pub_date}, fetch_time={self.fetch_time}, "
                f"text={self.text}, first_fetch_time={self.first_fetch_time})")


class DocumentProcessor:
    def __init__(self):
        self.documents: Dict[str, TDocument] = {}

    def process(self, doc: TDocument) -> Optional[TDocument]:
        if doc is None:
            return None

        existing_doc = self.documents.get(doc.url)

        if existing_doc:
            if doc.fetch_time > existing_doc.fetch_time:
                existing_doc.text = doc.text
                existing_doc.fetch_time = doc.fetch_time
            if doc.fetch_time < existing_doc.first_fetch_time:
                existing_doc.first_fetch_time = doc.fetch_time
            if doc.fetch_time < existing_doc.fetch_time:
                existing_doc.pub_date = doc.pub_date
        else:
            self.documents[doc.url] = doc

        return self.documents[doc.url]


# Пример использования
if __name__ == "__main__":
    processor = DocumentProcessor()

    docs = [
        TDocument(url="doc1", pub_date=10, fetch_time=100, text="Первая версия"),
        TDocument(url="doc1", pub_date=9, fetch_time=90, text="Старая версия"),
        TDocument(url="doc1", pub_date=11, fetch_time=110, text="Последняя версия")
    ]

    for doc in docs:
        updated_doc = processor.process(doc)
        print(f"Обработанный документ: {updated_doc}")
