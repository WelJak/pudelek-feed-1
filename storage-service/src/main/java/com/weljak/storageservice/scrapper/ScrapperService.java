package com.weljak.storageservice.scrapper;

import com.weljak.storageservice.webapi.ScrapperResponse;

public interface ScrapperService {
    public ScrapperResponse fetchEntryDetails(String url);
}
