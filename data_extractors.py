
class CommonDataExtractor:
    name_header = "NAME OF DRUG"
    registration_number_header = "NDA REGISTRATION NUMBER"
    license_holder_header = "LICENSE HOLDER"
    manufacturer_header = "MANUFACTURER"
    country_of_manufacture_header = "COUNTRY OF MANUFACTURE"
    local_technical_representative_header = "LOCAL TECHNICAL REPRESENTATIVE"
    dosage_form_header = "DOSAGE FORM"
    pack_size_header = "PACK SIZE"

    def __init__(self, table):
        self.data = []
        self.table = table
        self.headers_index = self.get_table_headers_indexes()

        self.set_headers()
        self.process_data()

    def get_unique_data(self):
        raise NotImplementedError

    def get_table_headers_indexes(self):
        return {
            header.text: index
            for index, header in enumerate(self.table.find("thead").find_all("th"))
        }

    def get_common_data(self, row_data):
        return {
            "name": row_data[self.headers_index[self.name_header]],
            "registration_number": row_data[self.headers_index[self.registration_number_header]],
            "license_holder": row_data[self.headers_index[self.license_holder_number_header]],
            "manufacturer": row_data[self.headers_index[self.manufacturer_header]],
            "country_of_manufacture": row_data[self.headers_index[self.country_of_manufacture_header]],
            "local_technical_representative": row_data[self.headers_index[self.local_technical_representative_header]],
            "dosage_form": row_data[self.headers_index[self.dosage_form_header]],
            "pack_size": row_data[self.headers_index[self.pack_size_header]]
        }

    def get_data(self, row_data):
        return {
            header[:-7]: row_data[self.headers_index[getattr(self, header)]]
            for header in self.headers
        }

    def process_data(self):
        for table_row in self.table.find("tbody").find_all("tr"):
            row_data = [column.text for column in table_row.find_all("td")]
            self.data.append(
                self.model_class(
                    **self.get_data(row_data)
                )
            )
        return self.data

    def set_headers(self):
        self.headers = [
            attribute for attribute in dir(self) if attribute.endswith("_header")
        ]


class HerbalHumanDataExtractor(CommonDataExtractor):
    sn_header = "S/N"
    registration_date_header = "REGISTRATION DATE"


class HerbalVetDataExtractor(CommonDataExtractor):
    registration_date_header = "REGISTRATION DATE"


class HumanDataExtractor(CommonDataExtractor):
    sn_header = "S/N"
    generic_name_header = "GENERIC NAME OF DRUG"
    strength_header = "STRENGTH OF DRUG"
    registration_date_header = "REGISTRATION DATE"


class VetDataExtractor(CommonDataExtractor):
    sn_header = "S/N"
    generic_name_header = "GENERIC NAME OF DRUG"
    strength_header = "STRENGTH OF DRUG"
    registration_date_header = "REGISTRATION DATE"


class LocalTraditionalHumanHerbalDataExtractor(CommonDataExtractor):
    sn_header = "S/N"
    license_holder_header = "LICENCE HOLDER"
    registration_number_header = "REGISTRATION NUMBER"
