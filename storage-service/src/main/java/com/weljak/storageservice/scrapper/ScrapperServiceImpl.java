package com.weljak.storageservice.scrapper;

import com.weljak.storageservice.webapi.ScrapperResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;
@Slf4j
@Service
@RequiredArgsConstructor
public class ScrapperServiceImpl implements ScrapperService {
    @Override
    public ScrapperResponse fetchEntryDetails(String url) {
        try {
            final Document document = Jsoup.connect(url).get();
            Elements title = document.getElementsByClass("sc-7hqr3i-0 am69kv-0 gNsebj");
            Elements creation_date = document.getElementsByClass("sc-7hqr3i-0 am69kv-0 px728r-0 iWBEYt");
            String entryid = url.substring(url.length() - 17);
            Elements description = document.getElementsByClass("sc-7hqr3i-0 am69kv-0 suku3l-0 eMCtfV");
            List<String> tags = new ArrayList<>();
            Elements rawtags = document.getElementsByClass("sc-7hqr3i-0 am69kv-0 sc-1pabckk-0 cOjdJX");
            for (Element element : rawtags) {
                tags.add(element.getElementsByClass("sc-7hqr3i-0 am69kv-0 sc-1pabckk-0 cOjdJX").text());
            }
            String type;
            if (url.contains("pudelek")) {
                type = "PUDELEK";
            } else {
                type = "TODO";
            }
            String uuid = UUID.randomUUID().toString();
            return new ScrapperResponse(uuid, type, entryid, creation_date.text(), title.text(), description.text(), tags, url);
        } catch (IOException ioe) {
            ioe.printStackTrace();
            return null;
        }
    }

}
