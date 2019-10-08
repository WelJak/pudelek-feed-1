package com.weljak.storageservice.news;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
<<<<<<< HEAD:storage-service/src/main/java/com/weljak/storageservice/message/Tags.java
import lombok.Setter;
import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;
=======
>>>>>>> 635806b779eda857df12dd7db05cbafcc80e28bb:storage-service/src/main/java/com/weljak/storageservice/news/Tags.java

import javax.persistence.*;


@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "tags")
public class Tags {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "tag", nullable = false)
    private String tag;

<<<<<<< HEAD:storage-service/src/main/java/com/weljak/storageservice/message/Tags.java
    @ManyToOne(fetch = FetchType.EAGER)
    @OnDelete(action = OnDeleteAction.CASCADE)
    @JoinColumn(name = "uuid", nullable = false)
    private News uuid;


=======
    @Column(name = "uuid")
    private String uuid;
>>>>>>> 635806b779eda857df12dd7db05cbafcc80e28bb:storage-service/src/main/java/com/weljak/storageservice/news/Tags.java
}
