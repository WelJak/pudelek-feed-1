package com.weljak.feeddashboard.service;

import com.weljak.feeddashboard.domain.News;

import java.util.List;

public interface EntriesRepository {
    List<News> listAllEntries();
    News getEntryDetails(String id);
}
