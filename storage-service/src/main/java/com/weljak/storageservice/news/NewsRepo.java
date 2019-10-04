package com.weljak.storageservice.news;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NewsRepo extends JpaRepository<News, String> {
    boolean existsByEntryid(String entryid);
}
