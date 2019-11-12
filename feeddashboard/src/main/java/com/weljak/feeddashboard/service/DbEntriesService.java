package com.weljak.feeddashboard.service;

import com.weljak.feeddashboard.domain.News;
import com.weljak.feeddashboard.repo.NewsRepo;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class DbEntriesService implements EntriesService {

    final NewsRepo newsRepo;

    @Override
    public List<News> listAllEntries() {
        String query = "SELECT description , title , entryid , link FROM news";
        List<News> entries = new ArrayList<>();
        newsRepo.findAll().forEach(entries::add);
        return entries;
    }
}
