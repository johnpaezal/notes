# Build Tools
*Manage dependencies, compile, test, and package Java projects*

## Maven

Project structure:
```
project/
  src/
    main/java/      ← source code
    test/java/      ← tests
  pom.xml           ← project config
```

### pom.xml

```xml
<project>
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.company</groupId>
  <artifactId>my-app</artifactId>
  <version>1.0.0</version>
  <packaging>jar</packaging>

  <properties>
    <java.version>21</java.version>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>5.10.0</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
</project>
```

### Common Commands

```bash
mvn compile          # compile source code
mvn test             # run tests
mvn package          # build JAR
mvn clean            # delete target/ folder
mvn clean install    # clean + build + install to local repo
mvn dependency:tree  # show dependency tree
```

---

## Gradle

Project structure:
```
project/
  src/
    main/java/      ← source code
    test/java/      ← tests
  build.gradle      ← project config (Groovy)
  build.gradle.kts  ← project config (Kotlin DSL)
```

### build.gradle (Kotlin DSL)

```kotlin
plugins {
    java
    application
}

group = "com.company"
version = "1.0.0"

java {
    sourceCompatibility = JavaVersion.VERSION_21
}

repositories {
    mavenCentral()
}

dependencies {
    testImplementation("org.junit.jupiter:junit-jupiter:5.10.0")
}

application {
    mainClass.set("com.company.Main")
}
```

### Common Commands

```bash
./gradlew build          # compile + test + package
./gradlew test           # run tests
./gradlew run            # run main class
./gradlew clean          # delete build/ folder
./gradlew dependencies   # show dependency tree
```

---

## Maven vs Gradle

| Feature     | Maven         | Gradle              |
|-------------|---------------|---------------------|
| Config      | XML (pom.xml) | Kotlin/Groovy DSL   |
| Speed       | Slower        | Faster (incremental)|
| Flexibility | Convention    | Highly customizable |
| Popularity  | Very common   | Growing (Android)   |
