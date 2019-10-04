package com.weljak.storageservice.message.newsrepo;

import com.weljak.storageservice.message.News;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface NewsRepo extends JpaRepository<News, String> {
    News findByUuid(String uuid);
    boolean existsByEntryid(String entryid);
}
