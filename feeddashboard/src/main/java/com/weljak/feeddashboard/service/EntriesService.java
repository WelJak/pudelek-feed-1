package com.weljak.feeddashboard.service;

import com.weljak.feeddashboard.domain.News;

import java.util.List;

public interface EntriesService {
    List<News> listAllEntries();
}
