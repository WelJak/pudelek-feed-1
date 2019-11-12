package com.weljak.feeddashboard.domain;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.List;

@Entity
@NoArgsConstructor
@AllArgsConstructor
@Table(name = "news")
@Builder
@Data
public class News {

    @Id
    @Column(name = "uuid", unique = true, nullable = false, updatable = false)
    private String uuid;

    @Column(name = "type", nullable = false)
    private String type;

    @Column(name = "entryid", nullable = false)
    private String entryid;

    @Column(name = "post_date", nullable = false)
    private String post_date;

    @Column(name = "title", nullable = false)
    private String title;

    @Column(name = "description", nullable = false)
    private String description;

    @OneToMany(
            cascade = CascadeType.ALL,
            orphanRemoval = true
    )
    @JoinColumn(name = "uuid")
    private List<Tags> tag;

    @Column(name = "link", nullable = false)
    private String link;

    @Column(name = "was_sent")
    private boolean wassent;
}
