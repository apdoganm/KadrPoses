import os
from pathlib import Path

PROJECT_ROOT = Path(".")

FILES = {
    "settings.gradle.kts": """pluginManagement {
    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}
rootProject.name = "KadrPoses"
include(":app")
""",

    "gradle.properties": """org.gradle.jvmargs=-Xmx3072m -Dfile.encoding=UTF-8
android.useAndroidX=true
kotlin.code.style=official
android.nonTransitiveRClass=true
""",

    "build.gradle.kts": """plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.kotlin.android) apply false
    alias(libs.plugins.kotlin.compose) apply false
    alias(libs.plugins.kotlin.serialization) apply false
    alias(libs.plugins.ksp) apply false
    alias(libs.plugins.hilt) apply false
}
""",

    "gradle/libs.versions.toml": """[versions]
agp = "8.7.2"
kotlin = "2.0.21"
ksp = "2.0.21-1.0.27"
coreKtx = "1.15.0"
appcompat = "1.7.0"
lifecycle = "2.8.7"
activityCompose = "1.9.3"
composeBom = "2024.11.00"
navigationCompose = "2.8.4"
hilt = "2.52"
hiltNavigationCompose = "1.2.0"
room = "2.6.1"
datastore = "1.1.1"
coroutines = "1.9.0"
serializationJson = "1.7.3"
coil = "2.7.0"
timber = "5.0.1"

[libraries]
androidx-core-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "coreKtx" }
androidx-appcompat = { group = "androidx.appcompat", name = "appcompat", version.ref = "appcompat" }
androidx-lifecycle-runtime-ktx = { group = "androidx.lifecycle", name = "lifecycle-runtime-ktx", version.ref = "lifecycle" }
androidx-lifecycle-runtime-compose = { group = "androidx.lifecycle", name = "lifecycle-runtime-compose", version.ref = "lifecycle" }
androidx-lifecycle-viewmodel-compose = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-compose", version.ref = "lifecycle" }
androidx-activity-compose = { group = "androidx.activity", name = "activity-compose", version.ref = "activityCompose" }

androidx-compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "composeBom" }
androidx-compose-ui = { group = "androidx.compose.ui", name = "ui" }
androidx-compose-ui-graphics = { group = "androidx.compose.ui", name = "ui-graphics" }
androidx-compose-ui-tooling = { group = "androidx.compose.ui", name = "ui-tooling" }
androidx-compose-ui-tooling-preview = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
androidx-compose-material3 = { group = "androidx.compose.material3", name = "material3" }
androidx-compose-material-icons = { group = "androidx.compose.material", name = "material-icons-extended" }

androidx-navigation-compose = { group = "androidx.navigation", name = "navigation-compose", version.ref = "navigationCompose" }

hilt-android = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-compiler = { group = "com.google.dagger", name = "hilt-android-compiler", version.ref = "hilt" }
androidx-hilt-navigation-compose = { group = "androidx.hilt", name = "hilt-navigation-compose", version.ref = "hiltNavigationCompose" }

room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
room-ktx = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
room-compiler = { group = "androidx.room", name = "room-compiler", version.ref = "room" }

datastore-preferences = { group = "androidx.datastore", name = "datastore-preferences", version.ref = "datastore" }
kotlinx-coroutines-android = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-android", version.ref = "coroutines" }
kotlinx-serialization-json = { group = "org.jetbrains.kotlinx", name = "kotlinx-serialization-json", version.ref = "serializationJson" }

coil-compose = { group = "io.coil-kt", name = "coil-compose", version.ref = "coil" }
timber = { group = "com.jakewharton.timber", name = "timber", version.ref = "timber" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }
ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
""",

    "app/build.gradle.kts": """plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
    alias(libs.plugins.kotlin.serialization)
    alias(libs.plugins.ksp)
    alias(libs.plugins.hilt)
}

android {
    namespace = "com.kadr.poses"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.kadr.poses"
        minSdk = 24
        targetSdk = 35
        versionCode = 1
        versionName = "1.0.0"
        vectorDrawables { useSupportLibrary = true }
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions { jvmTarget = "17" }

    buildFeatures {
        compose = true
        buildConfig = true
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.lifecycle.runtime.compose)
    implementation(libs.androidx.lifecycle.viewmodel.compose)
    implementation(libs.androidx.activity.compose)

    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.compose.ui)
    implementation(libs.androidx.compose.ui.graphics)
    implementation(libs.androidx.compose.ui.tooling.preview)
    implementation(libs.androidx.compose.material3)
    implementation(libs.androidx.compose.material.icons)
    debugImplementation(libs.androidx.compose.ui.tooling)

    implementation(libs.androidx.navigation.compose)
    implementation(libs.hilt.android)
    ksp(libs.hilt.compiler)
    implementation(libs.androidx.hilt.navigation.compose)

    implementation(libs.room.runtime)
    implementation(libs.room.ktx)
    ksp(libs.room.compiler)

    implementation(libs.datastore.preferences)
    implementation(libs.kotlinx.coroutines.android)
    implementation(libs.kotlinx.serialization.json)
    implementation(libs.coil.compose)
    implementation(libs.timber)
}
""",

    "app/proguard-rules.pro": """-keepattributes *Annotation*,InnerClasses
-dontnote kotlinx.serialization.AnnotationsKt
-keep,includedescriptorclasses class com.kadr.poses.**$$serializer { *; }
-keepclassmembers class com.kadr.poses.** { *** Companion; }
-keepclasseswithmembers class com.kadr.poses.** { kotlinx.serialization.KSerializer serializer(...); }
""",

    "app/src/main/res/xml/locales_config.xml": """<?xml version="1.0" encoding="utf-8"?>
<locale-config xmlns:android="http://schemas.android.com/apk/res/android">
    <locale android:name="en" />
    <locale android:name="ar" />
</locale-config>
""",

    "app/src/main/AndroidManifest.xml": """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <application
        android:name=".KadrApplication"
        android:allowBackup="true"
        android:icon="@android:drawable/ic_menu_camera"
        android:label="@string/app_name"
        android:localeConfig="@xml/locales_config"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.DayNight.NoActionBar">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        <service
            android:name="androidx.appcompat.app.AppLocalesMetadataHolderService"
            android:enabled="false"
            android:exported="false">
            <meta-data android:name="autoStoreLocales" android:value="true" />
        </service>
    </application>
</manifest>
""",

    "app/src/main/res/values/strings.xml": """<resources>
    <string name="app_name">Kadr</string>
    <string name="nav_home">Home</string>
    <string name="nav_poses">Poses</string>
    <string name="nav_shot_lists">Shot Lists</string>
    <string name="nav_saved">Saved</string>
    <string name="nav_settings">Settings</string>
    <string name="onboarding_skip">Skip</string>
    <string name="onboarding_next">Next</string>
    <string name="onboarding_start">Start Directing</string>
    <string name="onboarding_title_1">Direct Effortless Wedding Poses</string>
    <string name="onboarding_desc_1">Browse modern wedding poses with clear visual guides and verbal cues for the couple.</string>
    <string name="onboarding_title_2">Pro Camera Specs at a Glance</string>
    <string name="onboarding_desc_2">Includes focal length, aperture, shutter speed, lighting angle, and mistakes to avoid.</string>
    <string name="onboarding_title_3">Offline Shot Lists &amp; Shoot Mode</string>
    <string name="onboarding_desc_3">Plan custom timelines and use high-contrast Shoot Mode with one hand on wedding day.</string>
    <string name="home_greeting">Ready for Today\'s Shoot</string>
    <string name="home_subtitle">Pocket Wedding Pose Director</string>
    <string name="home_pose_of_day">Pose of the Day</string>
    <string name="home_categories">Quick Categories</string>
    <string name="home_continue_list">Active Shot List</string>
    <string name="home_trending">Trending Poses</string>
    <string name="home_see_all">See All</string>
    <string name="filter_all">All</string>
    <string name="subject_bride_solo">Bride Solo</string>
    <string name="subject_couple">Couple</string>
    <string name="subject_details">Details &amp; Dress</string>
    <string name="difficulty_easy">Easy</string>
    <string name="difficulty_medium">Medium</string>
    <string name="difficulty_advanced">Advanced</string>
    <string name="location_indoor">Indoor</string>
    <string name="location_outdoor">Outdoor</string>
    <string name="location_studio">Studio</string>
    <string name="mood_romantic">Romantic</string>
    <string name="mood_playful">Playful</string>
    <string name="mood_editorial">Editorial</string>
    <string name="mood_cinematic">Cinematic</string>
    <string name="sort_default">Recommended</string>
    <string name="sort_difficulty">By Difficulty</string>
    <string name="sort_alphabetical">Alphabetical</string>
    <string name="search_hint">Search poses, lenses, or moods…</string>
    <string name="clear_filters">Reset Filters</string>
    <string name="empty_library_title">No Matching Poses</string>
    <string name="empty_library_subtitle">Try clearing a filter chip or searching with a broader keyword.</string>
    <string name="director_cue_label">Director Cue (Say to the couple):</string>
    <string name="steps_section_title">Step-by-Step Directions</string>
    <string name="tips_section_title">Photographer Specs &amp; Lighting</string>
    <string name="mistakes_section_title">Common Mistakes to Avoid</string>
    <string name="dress_fit_label">Best Dress Silhouettes</string>
    <string name="props_label">Suggested Props</string>
    <string name="action_add_to_list">Add to Shot List</string>
    <string name="action_enter_shoot_mode">Shoot Mode</string>
    <string name="action_share">Share Pose</string>
    <string name="action_favorite_toggle">Toggle Favorite</string>
    <string name="added_to_shot_list">Added to shot list</string>
    <string name="shoot_mode_exit">Exit</string>
    <string name="shoot_mode_counter">Pose %1$d of %2$d</string>
    <string name="shoot_mode_prev">Previous</string>
    <string name="shoot_mode_next">Next</string>
    <string name="shoot_mode_done">Completed</string>
    <string name="shot_list_new">New Shot List</string>
    <string name="shot_list_name_hint">e.g., Golden Hour Portraits</string>
    <string name="shot_list_create">Create</string>
    <string name="shot_list_cancel">Cancel</string>
    <string name="shot_list_progress">%1$d / %2$d Completed</string>
    <string name="shot_list_empty_title">No Shot Lists Yet</string>
    <string name="shot_list_empty_subtitle">Create a list for Bridal Prep or Golden Hour to organize your shoot day.</string>
    <string name="saved_empty_title">No Saved Poses Yet</string>
    <string name="saved_empty_subtitle">Tap the heart icon on any pose card to bookmark it offline.</string>
    <string name="saved_explore_cta">Explore Pose Library</string>
    <string name="settings_language">App Language</string>
    <string name="settings_lang_ar">العربية (Arabic - RTL)</string>
    <string name="settings_lang_en">English (LTR)</string>
    <string name="settings_theme">Appearance</string>
    <string name="settings_theme_light">Light (Warm Ivory - Default)</string>
    <string name="settings_theme_dark">Dark (Charcoal Studio)</string>
    <string name="settings_theme_system">Follow System</string>
    <string name="settings_about_title">About Kadr v1.0.0</string>
    <string name="settings_about_desc">100% Offline-First Pocket Pose Director. Zero tracking, zero ads.</string>
    <string name="back_button_desc">Navigate back</string>
</resources>
""",

    "app/src/main/res/values-ar/strings.xml": """<resources>
    <string name="app_name">كادر</string>
    <string name="nav_home">الرئيسية</string>
    <string name="nav_poses">الوضعيات</string>
    <string name="nav_shot_lists">قوائم التصوير</string>
    <string name="nav_saved">المحفوظات</string>
    <string name="nav_settings">الإعدادات</string>
    <string name="onboarding_skip">تخطي</string>
    <string name="onboarding_next">التالي</string>
    <string name="onboarding_start">ابدأ التوجيه</string>
    <string name="onboarding_title_1">وجّه وضعيات الزفاف باحترافية وسلاسة</string>
    <string name="onboarding_desc_1">تصفح أحدث وضعيات الزفاف العصرية مع رسوم توضيحية واضحة وجمل توجيهية للعروسين.</string>
    <string name="onboarding_title_2">إعدادات الكاميرا والإضاءة في لمحة</string>
    <string name="onboarding_desc_2">تتضمن كل وضعية البعد البؤري، فتحة العدسة، سرعة الغالق، زاوية الإضاءة، والأخطاء الشائعة.</string>
    <string name="onboarding_title_3">قوائم تصوير بدون إنترنت ووضع التصوير الحي</string>
    <string name="onboarding_desc_3">خطط لجلسة الساعة الذهبية واستخدم وضع التصوير عالي التباين بيد واحدة يوم الزفاف.</string>
    <string name="home_greeting">جاهز لجلسة تصوير اليوم؟</string>
    <string name="home_subtitle">دليلك الجيبي لتوجيه وضعيات الزفاف</string>
    <string name="home_pose_of_day">وضعية اليوم المختارة</string>
    <string name="home_categories">التصنيفات السريعة</string>
    <string name="home_continue_list">قائمة التصوير النشطة</string>
    <string name="home_trending">الوضعيات الرائجة</string>
    <string name="home_see_all">عرض الكل</string>
    <string name="filter_all">الكل</string>
    <string name="subject_bride_solo">العروس منفردة</string>
    <string name="subject_couple">العروسان</string>
    <string name="subject_details">تفاصيل وفستان</string>
    <string name="difficulty_easy">سهل</string>
    <string name="difficulty_medium">متوسط</string>
    <string name="difficulty_advanced">متقدم</string>
    <string name="location_indoor">داخلي</string>
    <string name="location_outdoor">خارجي</string>
    <string name="location_studio">استوديو</string>
    <string name="mood_romantic">رومانسي</string>
    <string name="mood_playful">مرح</string>
    <string name="mood_editorial">تحريري</string>
    <string name="mood_cinematic">سينمائي</string>
    <string name="sort_default">المقترح</string>
    <string name="sort_difficulty">حسب الصعوبة</string>
    <string name="sort_alphabetical">أبجدياً</string>
    <string name="search_hint">ابحث عن وضعية، عدسة، أو طابع…</string>
    <string name="clear_filters">إعادة ضبط الفلاتر</string>
    <string name="empty_library_title">لا توجد وضعيات مطابقة</string>
    <string name="empty_library_subtitle">جرّب إزالة بعض الفلاتر أو البحث بكلمة أخرى.</string>
    <string name="director_cue_label">توجيه المصور (قل للعروسين):</string>
    <string name="steps_section_title">الخطوات التفصيلية للوضعية</string>
    <string name="tips_section_title">إعدادات الكاميرا والإضاءة</string>
    <string name="mistakes_section_title">أخطاء شائعة يجب تجنبها</string>
    <string name="dress_fit_label">قصات الفستان المناسبة</string>
    <string name="props_label">الإكسسوارات المقترحة</string>
    <string name="action_add_to_list">إضافة لقائمة تصوير</string>
    <string name="action_enter_shoot_mode">وضع التصوير</string>
    <string name="action_share">مشاركة الوضعية</string>
    <string name="action_favorite_toggle">تبديل المفضلة</string>
    <string name="added_to_shot_list">تمت الإضافة إلى قائمة التصوير</string>
    <string name="shoot_mode_exit">خروج</string>
    <string name="shoot_mode_counter">وضعية %1$d من %2$d</string>
    <string name="shoot_mode_prev">السابق</string>
    <string name="shoot_mode_next">التالي</string>
    <string name="shoot_mode_done">مكتملة</string>
    <string name="shot_list_new">قائمة تصوير جديدة</string>
    <string name="shot_list_name_hint">مثال: جلسة الساعة الذهبية</string>
    <string name="shot_list_create">إنشاء</string>
    <string name="shot_list_cancel">إلغاء</string>
    <string name="shot_list_progress">اكتمل %1$d من %2$d</string>
    <string name="shot_list_empty_title">لا توجد قوائم تصوير بعد</string>
    <string name="shot_list_empty_subtitle">أنشئ قائمة مخصصة للتجهيزات أو الساعة الذهبية لترتيب لقطات يوم الزفاف.</string>
    <string name="saved_empty_title">لا توجد وضعيات محفوظة</string>
    <string name="saved_empty_subtitle">اضغط على أيقونة القلب في أي وضعية لحفظها هنا والوصول إليها بدون إنترنت.</string>
    <string name="saved_explore_cta">استكشف مكتبة الوضعيات</string>
    <string name="settings_language">لغة التطبيق</string>
    <string name="settings_lang_ar">العربية (RTL)</string>
    <string name="settings_lang_en">English (LTR)</string>
    <string name="settings_theme">المظهر</string>
    <string name="settings_theme_light">فاتح (عاجي دافئ - افتراضي)</string>
    <string name="settings_theme_dark">داكن (استوديو فحمي)</string>
    <string name="settings_theme_system">تلقائي حسب النظام</string>
    <string name="settings_about_title">حول تطبيق كادر v1.0.0</string>
    <string name="settings_about_desc">يعمل 100% بدون إنترنت. بدون إعلانات أو تتبع.</string>
    <string name="back_button_desc">رجوع</string>
</resources>
""",

    "app/src/main/assets/poses_seed.json": """[
  {
    "id": "pose_01",
    "assetName": "pose_01",
    "nameAr": "عناق الخلف وقبلة الوجنة",
    "nameEn": "Back-Embrace Cheek Kiss",
    "shortDescriptionAr": "عناق دافئ من الخلف مع قبلة هادئة على الوجنة تبرز ملامح الفرح والسكينة.",
    "shortDescriptionEn": "Warm back-hug with a gentle cheek kiss highlighting serene joy.",
    "category": "CLOSE_UP",
    "subject": "COUPLE",
    "difficulty": "EASY",
    "moodTags": ["ROMANTIC"],
    "locationTags": ["INDOOR", "STUDIO"],
    "bestForDressSilhouettesAr": ["قصة A-Line", "ياقة القلب", "أكمام منفوخة"],
    "bestForDressSilhouettesEn": ["A-Line", "Sweetheart Neckline", "Puff Sleeves"],
    "stepsAr": [
      "تقف العروس باتجاه الكاميرا بزاوية خفيفة 15 درجة.",
      "يقف العريس خلفها مباشرة ويلف ذراعيه حول خصرها فوق الباقة.",
      "تمسك العروس باقة الزهور البيضاء بكلتا يديها عند مستوى الخصر.",
      "يميل العريس برأسه ليطبع قبلة ناعمة على وجنة العروس اليسرى.",
      "ترفع العروس ذقنها قليلاً وتغمض عينيها بابتسامة هادئة."
    ],
    "stepsEn": [
      "Bride stands facing camera at a slight 15-degree angle.",
      "Groom stands directly behind, wrapping arms around her waist.",
      "Bride holds the white bouquet at waist level with both hands.",
      "Groom leans in to press a gentle kiss on her cheek.",
      "Bride tilts chin slightly up and closes eyes with a soft smile."
    ],
    "photographerTips": {
      "angleAr": "مستوى العين",
      "angleEn": "Eye-level",
      "lensMm": "85mm",
      "distanceAr": "1.5 متر (كادر نصفي)",
      "distanceEn": "1.5m (Medium close-up)",
      "lightingAr": "إضاءة جانبية ناعمة بزاوية 45 درجة",
      "lightingEn": "Soft 45-degree key light",
      "compositionAr": "توسيط العروسين مع ترك مساحة علوية 25%",
      "compositionEn": "Center subjects with 25% headroom",
      "suggestedAperture": "f/2.0",
      "suggestedShutter": "1/320s"
    },
    "propsAr": ["باقة زهور أقحوان بيضاء صغيرة", "تاج زهور ناعم للشعر"],
    "propsEn": ["Small white daisy bouquet", "Delicate floral hair crown"],
    "commonMistakesAr": ["ضغط ذقن العريس بقوة على خد العروس.", "رفع الباقة عالياً فتغطي ياقة الفستان."],
    "commonMistakesEn": ["Groom pressing too hard into bride's cheek.", "Holding bouquet too high."],
    "directorCueAr": "احتضنها من الخلف واقترب ببطء لقبلة هادئة على الوجنة، وارفعي ذقنك قليلاً مع إغماض عينيك.",
    "directorCueEn": "Wrap your arms around her waist for a slow cheek kiss; Bride, tilt your chin up and close your eyes.",
    "illustrationSpec": {
      "framing": "Medium three-quarter portrait from hips up",
      "figuresPosition": "Groom behind bride kissing her cheek",
      "colorPalette": ["#2F343A", "#FFFFFF", "#C8C9CD", "#FCE0D2", "#F2A7A7"],
      "backgroundTint": "BLUSH"
    },
    "imageGenerationPrompt": "Flat vector cel-shaded wedding illustration on solid dark charcoal background #2F343A."
  },
  {
    "id": "pose_02",
    "assetName": "pose_02",
    "nameAr": "خطوة الفالس العفوية",
    "nameEn": "Candid Crosswalk Stride",
    "shortDescriptionAr": "مشية حيوية يداً بيد مع التفاتة متبادلة تمنح الصورة حركة طبيعية.",
    "shortDescriptionEn": "Dynamic hand-in-hand walk with a shared glance for natural motion.",
    "category": "WALKING",
    "subject": "COUPLE",
    "difficulty": "EASY",
    "moodTags": ["PLAYFUL", "EDITORIAL"],
    "locationTags": ["OUTDOOR"],
    "bestForDressSilhouettesAr": ["قصة A-Line", "فستان منسدل"],
    "bestForDressSilhouettesEn": ["A-Line", "Flowy Gown"],
    "stepsAr": [
      "يمشي العروسان للأمام بخطوات بطيئة ومتزامنة.",
      "يمسك العريس يد العروس اليمنى بيده اليسرى.",
      "يضع العريس يده اليمنى داخل جيب البنطلون بأناقة.",
      "تحمل العروس الباقة بيدها اليسرى منخفضة بجانب الفستان.",
      "ينظر العروسان لبعضهما مع ضحكة خفيفة أثناء الخطوة."
    ],
    "stepsEn": [
      "Couple walks forward in slow synchronized steps.",
      "Groom holds bride's right hand loosely with his left.",
      "Groom tucks his right hand into his trouser pocket.",
      "Bride carries bouquet low at her left side.",
      "Both look at each other mid-stride with a soft laugh."
    ],
    "photographerTips": {
      "angleAr": "منخفضة قليلاً لإبراز الطول",
      "angleEn": "Slightly low angle",
      "lensMm": "35mm",
      "distanceAr": "3 أمتار",
      "distanceEn": "3m",
      "lightingAr": "إضاءة الساعة الذهبية الخلفية",
      "lightingEn": "Golden hour backlight",
      "compositionAr": "قاعدة الأثلاث مع مساحة للحركة",
      "compositionEn": "Rule of thirds with leading space",
      "suggestedAperture": "f/2.8",
      "suggestedShutter": "1/1000s"
    },
    "propsAr": ["باقة زهور بيضاء"],
    "propsEn": ["White floral bouquet"],
    "commonMistakesAr": ["النظر إلى الأرض أثناء المشي.", "المشي بسرعة كبيرة."],
    "commonMistakesEn": ["Looking down at the ground.", "Walking too fast."],
    "directorCueAr": "امشيا نحوي ببطء شديد وكأنكما تتنزهان، وانظرا لبعضكما عند العد إلى ثلاثة.",
    "directorCueEn": "Stroll slowly toward me hand-in-hand, and look at each other on the count of three.",
    "illustrationSpec": {
      "framing": "Three-quarter length portrait",
      "figuresPosition": "Couple walking hand in hand",
      "colorPalette": ["#2F343A", "#FFFFFF", "#C8C9CD", "#FCE0D2", "#F2A7A7"],
      "backgroundTint": "SAGE"
    },
    "imageGenerationPrompt": "Flat vector cel-shaded wedding walk illustration on #2F343A."
  },
  {
    "id": "pose_03",
    "assetName": "pose_03",
    "nameAr": "التفاتة الكتف الحالمة",
    "nameEn": "Over-the-Shoulder Whisper",
    "shortDescriptionAr": "بورتريه فردي للعروس يبرز تصميم الظهر والأكمام المنفوخة وتاج الزهور.",
    "shortDescriptionEn": "Solo bridal portrait showcasing back details, puff sleeves, and floral crown.",
    "category": "STANDING",
    "subject": "BRIDE_SOLO",
    "difficulty": "EASY",
    "moodTags": ["EDITORIAL", "ROMANTIC"],
    "locationTags": ["INDOOR", "STUDIO"],
    "bestForDressSilhouettesAr": ["أكمام منفوخة", "ظهر مفتوح"],
    "bestForDressSilhouettesEn": ["Puff Sleeves", "Open Back"],
    "stepsAr": [
      "تقف العروس معطيًة ظهرها للكاميرا بزاوية 45 درجة.",
      "تلتفت برأسها وكتفيها ببطء نحو الكاميرا.",
      "تضم الباقة بالقرب من الصدر بيد واحدة.",
      "تخفض الكتف القريب من الكاميرا لإطالة خط العنق.",
      "تنظر نحو العدسة بنظرة هادئة وابتسامة ناعمة."
    ],
    "stepsEn": [
      "Bride stands angled 45 degrees away from the camera.",
      "Slowly turns head and upper torso back toward the lens.",
      "Holds bouquet near chest with one hand.",
      "Drops front shoulder slightly to elongate the neckline.",
      "Looks calmly into the lens with a gentle smile."
    ],
    "photographerTips": {
      "angleAr": "مستوى العين",
      "angleEn": "Eye-level",
      "lensMm": "50mm",
      "distanceAr": "2 متر",
      "distanceEn": "2m",
      "lightingAr": "إضاءة نافذة جانبية ناعمة",
      "lightingEn": "Soft side window light",
      "compositionAr": "وضع عين العروس على خط الثلث العلوي",
      "compositionEn": "Place bride's eye on upper third line",
      "suggestedAperture": "f/1.8",
      "suggestedShutter": "1/250s"
    },
    "propsAr": ["تاج زهور أبيض", "أقراط لؤلؤ"],
    "propsEn": ["White floral crown", "Pearl earrings"],
    "commonMistakesAr": ["لف الرقبة بزاوية حادة جداً.", "رفع الكتف الأمامي نحو الأذن."],
    "commonMistakesEn": ["Twisting neck too far.", "Hunching the front shoulder."],
    "directorCueAr": "قفي باتجاه النافذة، ثم التفتي نحوي ببطء من فوق كتفك وكأن أحداً نادى اسمك بهدوء.",
    "directorCueEn": "Face the window, then slowly look back over your shoulder as if someone softly called your name.",
    "illustrationSpec": {
      "framing": "Medium portrait from waist up",
      "figuresPosition": "Solo bride looking over shoulder",
      "colorPalette": ["#2F343A", "#FFFFFF", "#FCE0D2", "#F2A7A7"],
      "backgroundTint": "MIST"
    },
    "imageGenerationPrompt": "Flat vector solo bride over shoulder on #2F343A."
  },
  {
    "id": "pose_04",
    "assetName": "pose_04",
    "nameAr": "استراحة السلم الكلاسيكي",
    "nameEn": "Grand Staircase Lounge",
    "shortDescriptionAr": "جلسة غير متماثلة على الدرج تمنح طابعاً سينمائياً فخماً ومريحاً.",
    "shortDescriptionEn": "Asymmetrical seated pose on steps for an effortless editorial look.",
    "category": "SITTING",
    "subject": "COUPLE",
    "difficulty": "MEDIUM",
    "moodTags": ["CINEMATIC", "EDITORIAL"],
    "locationTags": ["INDOOR"],
    "bestForDressSilhouettesAr": ["قصة A-Line", "فستان ملكي واسع"],
    "bestForDressSilhouettesEn": ["A-Line", "Ballgown"],
    "stepsAr": [
      "تجلس العروس على درجة السلم مع فرد طيات الفستان.",
      "يجلس العريس على الدرجة الأعلى خلفها بقليل.",
      "يسند العريس مرفقه على ركبته ويميل نحو العروس.",
      "تتكئ العروس بكتفها على ساق العريس وتضع الباقة في حجرها.",
      "يتبادلان نظرة هادئة من زاوية جانبية."
    ],
    "stepsEn": [
      "Bride sits on a step with skirt draped over the lower stair.",
      "Groom sits one step higher behind her.",
      "Groom rests elbow on his knee, leaning toward the bride.",
      "Bride leans her shoulder against groom's leg.",
      "Both share a calm profile gaze."
    ],
    "photographerTips": {
      "angleAr": "من مستوى الدرجة السفلية",
      "angleEn": "Low angle from lower step",
      "lensMm": "50mm",
      "distanceAr": "2.5 متر",
      "distanceEn": "2.5m",
      "lightingAr": "إضاءة علوية دافئة",
      "lightingEn": "Warm overhead light",
      "compositionAr": "تكوين مثلثي",
      "compositionEn": "Triangular composition",
      "suggestedAperture": "f/2.2",
      "suggestedShutter": "1/200s"
    },
    "propsAr": ["باقة زهور بيضاء"],
    "propsEn": ["White floral bouquet"],
    "commonMistakesAr": ["انحناء الظهر أثناء الجلوس.", "تكدس الفستان تحت القدمين."],
    "commonMistakesEn": ["Slouching lower back.", "Bunching dress fabric."],
    "directorCueAr": "اجلسا براحة على الدرج، افردي فستانك على الدرجة السفلية واتكئي بكتفك على العريس.",
    "directorCueEn": "Sit comfortably on the steps, drape your skirt down, and lean back against his shoulder.",
    "illustrationSpec": {
      "framing": "Three-quarter seated portrait",
      "figuresPosition": "Couple seated on stairs",
      "colorPalette": ["#2F343A", "#FFFFFF", "#C8C9CD", "#F2A7A7"],
      "backgroundTint": "MIST"
    },
    "imageGenerationPrompt": "Flat vector seated wedding couple on #2F343A."
  },
  {
    "id": "pose_05",
    "assetName": "pose_05",
    "nameAr": "نسيم الطرحة الذهبي",
    "nameEn": "Golden Hour Veil Breeze",
    "shortDescriptionAr": "وقفة شاعرية للعروس ترفع فيها طرف الطرحة أو التاج لتلتقط حركة الهواء.",
    "shortDescriptionEn": "Poetic solo bride pose touching floral crown in the breeze.",
    "category": "STANDING",
    "subject": "BRIDE_SOLO",
    "difficulty": "MEDIUM",
    "moodTags": ["ROMANTIC", "CINEMATIC"],
    "locationTags": ["OUTDOOR"],
    "bestForDressSilhouettesAr": ["قصة الحورية", "قصة A-Line"],
    "bestForDressSilhouettesEn": ["Mermaid", "A-Line"],
    "stepsAr": [
      "تقف العروس في مواجهة النسيم بزاوية 30 درجة.",
      "تمسك الباقة بيدها اليمنى عند مستوى الحوض.",
      "ترفع يدها اليسرى بلطف لتلامس تاج الزهور.",
      "تغمض عينيها بسلام.",
      "تأخذ نفساً عميقاً بابتسامة خفيفة."
    ],
    "stepsEn": [
      "Bride stands angled 30 degrees into the breeze.",
      "Holds bouquet at hip level with right hand.",
      "Gently raises left hand to touch floral crown.",
      "Closes eyes peacefully.",
      "Takes a deep breath with a soft smile."
    ],
    "photographerTips": {
      "angleAr": "مستوى الصدر",
      "angleEn": "Chest-level",
      "lensMm": "85mm",
      "distanceAr": "2 متر",
      "distanceEn": "2m",
      "lightingAr": "أشعة غروب خلفية",
      "lightingEn": "Sunset backlight",
      "compositionAr": "ترك مساحة فارغة في اتجاه النظر",
      "compositionEn": "Negative space in gaze direction",
      "suggestedAperture": "f/1.8",
      "suggestedShutter": "1/800s"
    },
    "propsAr": ["تاج زهور", "باقة أقحوان"],
    "propsEn": ["Floral crown", "Daisy bouquet"],
    "commonMistakesAr": ["شد الأصابع بقوة.", "تقطيب الحاجبين من الشمس."],
    "commonMistakesEn": ["Stiff fingers.", "Squinting into harsh sun."],
    "directorCueAr": "ارفعي يدك بلمسة خفيفة نحو تاج الزهور، أغمضي عينيك واستشعري نسمة الهواء.",
    "directorCueEn": "Lightly touch your floral crown, close your eyes, and enjoy the breeze.",
    "illustrationSpec": {
      "framing": "Waist up",
      "figuresPosition": "Solo bride touching floral crown",
      "colorPalette": ["#2F343A", "#FFFFFF", "#FCE0D2", "#F2A7A7"],
      "backgroundTint": "BLUSH"
    },
    "imageGenerationPrompt": "Flat vector solo bride touching crown on #2F343A."
  },
  {
    "id": "pose_06",
    "assetName": "pose_06",
    "nameAr": "همسة الجبين المتقارب",
    "nameEn": "Forehead Rest & Whisper",
    "shortDescriptionAr": "تلامس الجبينين في لقطة قريبة تركز على المشاعر الصادقة والهدوء.",
    "shortDescriptionEn": "Intimate forehead-to-forehead close-up focusing on quiet emotion.",
    "category": "CLOSE_UP",
    "subject": "COUPLE",
    "difficulty": "EASY",
    "moodTags": ["ROMANTIC"],
    "locationTags": ["OUTDOOR", "INDOOR"],
    "bestForDressSilhouettesAr": ["جميع القصات", "ياقة القلب"],
    "bestForDressSilhouettesEn": ["All Silhouettes", "Sweetheart Neckline"],
    "stepsAr": [
      "يقف العروسان متقابلين وجهاً لوجه بمسافة قريبة.",
      "يضع العريس يده في جيبه واليد الأخرى خلف خصر العروس.",
      "تضع العروس يدها بلطف على طية سترة العريس الرمادية.",
      "يميلان برأسيهما حتى يتلامس الجبينان برفق.",
      "يغمض العروسان أعينهما مع ابتسامة دافئة."
    ],
    "stepsEn": [
      "Couple stands facing each other closely.",
      "Groom keeps one hand in pocket, other on bride's waist.",
      "Bride rests her hand lightly on groom's gray lapel.",
      "Both lean forward until foreheads gently touch.",
      "Both close their eyes with a warm smile."
    ],
    "photographerTips": {
      "angleAr": "مستوى العين تماماً",
      "angleEn": "Strict eye-level",
      "lensMm": "85mm",
      "distanceAr": "1.2 متر",
      "distanceEn": "1.2m",
      "lightingAr": "إضاءة ناعمة متساوية",
      "lightingEn": "Even diffused light",
      "compositionAr": "ملء الكادر بالوجهين والأكتاف",
      "compositionEn": "Tight framing on faces",
      "suggestedAperture": "f/2.4",
      "suggestedShutter": "1/400s"
    },
    "propsAr": ["باقة زهور صغيرة"],
    "propsEn": ["Small floral bouquet"],
    "commonMistakesAr": ["تصادم الأنوف.", "إخفاء اليدين بالكامل."],
    "commonMistakesEn": ["Bumping noses.", "Hiding hands out of frame."],
    "directorCueAr": "اقتربا حتى يتلامس جبيناكما، ضعي يدك على صدره وأغمضا أعينكما لثانية هادئة.",
    "directorCueEn": "Lean in until your foreheads touch, rest your hand on his lapel, and close your eyes.",
    "illustrationSpec": {
      "framing": "Tight chest-up close-up",
      "figuresPosition": "Forehead touch close-up",
      "colorPalette": ["#2F343A", "#FFFFFF", "#C8C9CD", "#F2A7A7"],
      "backgroundTint": "BLUSH"
    },
    "imageGenerationPrompt": "Flat vector couple forehead touch on #2F343A."
  },
  {
    "id": "pose_07",
    "assetName": "pose_07",
    "nameAr": "انسياب الطيات وباقة الأقحوان",
    "nameEn": "Pleated Skirt & Daisy Bouquet",
    "shortDescriptionAr": "لقطة تفصيلية فنية ليدي العروس وهما تحتضنان باقة الزهور فوق طيات الفستان.",
    "shortDescriptionEn": "Artistic detail shot of bride's hands cradling the bouquet against pleated skirt.",
    "category": "CLOSE_UP",
    "subject": "DETAILS",
    "difficulty": "EASY",
    "moodTags": ["ROMANTIC", "EDITORIAL"],
    "locationTags": ["INDOOR", "OUTDOOR"],
    "bestForDressSilhouettesAr": ["تنورة بطيات", "قصة A-Line"],
    "bestForDressSilhouettesEn": ["Pleated Skirt", "A-Line"],
    "stepsAr": [
      "تقف العروس بوضعية مستقيمة ومسترخية.",
      "تمسك سيقان باقة الأقحوان البيضاء بكلتا يديها أمام الخصر.",
      "تتشابك الأصابع برقة دون شد المفاصل.",
      "تُمال الباقة قليلاً للأمام لإظهار الزهور.",
      "يتم ترتيب طيات تنورة الفستان البيضاء خلف اليدين."
    ],
    "stepsEn": [
      "Bride stands upright and relaxed.",
      "Holds white daisy bouquet stems at waist.",
      "Fingers overlap gently without tension.",
      "Tilts bouquet slightly forward to show blooms.",
      "Arranges white skirt pleats symmetrically."
    ],
    "photographerTips": {
      "angleAr": "ميل خفيف من الأعلى 15 درجة",
      "angleEn": "Slight 15-degree high angle",
      "lensMm": "50mm",
      "distanceAr": "0.8 متر",
      "distanceEn": "0.8m",
      "lightingAr": "إضاءة جانبية تبرز طيات الفستان",
      "lightingEn": "Side light accentuating folds",
      "compositionAr": "توسيط الباقة واليدين",
      "compositionEn": "Center hands and bouquet",
      "suggestedAperture": "f/2.8",
      "suggestedShutter": "1/320s"
    },
    "propsAr": ["باقة زهور أقحوان بيضاء"],
    "propsEn": ["White daisy bouquet"],
    "commonMistakesAr": ["الضغط القوي على السيقان.", "توجيه الزهور للأسفل."],
    "commonMistakesEn": ["Gripping stems tightly.", "Pointing flowers downward."],
    "directorCueAr": "أمسكي الباقة برفق عند خصرك وأميلي الزهور قليلاً نحوي.",
    "directorCueEn": "Cradle the bouquet softly at your waist and tilt the blooms toward the camera.",
    "illustrationSpec": {
      "framing": "Tight detail crop on hands and skirt",
      "figuresPosition": "Hands holding daisy bouquet",
      "colorPalette": ["#2F343A", "#FFFFFF", "#D0D3D8", "#FCE0D2"],
      "backgroundTint": "SAND"
    },
    "imageGenerationPrompt": "Flat vector detail of bride hands holding daisy bouquet on #2F343A."
  },
  {
    "id": "pose_08",
    "assetName": "pose_08",
    "nameAr": "دوران الفرح المعماري",
    "nameEn": "The Spin & Laugh Dip",
    "shortDescriptionAr": "حركة دوران مرحة تنشر تنورة الفستان وتلتقط ضحكة حقيقية بين العروسين.",
    "shortDescriptionEn": "Joyful spin flaring the wedding skirt and capturing genuine laughter.",
    "category": "WALKING",
    "subject": "COUPLE",
    "difficulty": "ADVANCED",
    "moodTags": ["PLAYFUL", "CINEMATIC"],
    "locationTags": ["OUTDOOR"],
    "bestForDressSilhouettesAr": ["قصة A-Line", "تنورة واسعة"],
    "bestForDressSilhouettesEn": ["A-Line", "Full Skirt"],
    "stepsAr": [
      "يقف العريس ثابتاً ويرفع يده اليسرى فوق رأس العروس.",
      "تمسك العروس بيده وتدور ببطء تحت ذراعه.",
      "تحمل العروس الباقة باليد الأخرى لتوازن الحركة.",
      "يثبت العريس خصرها بيده اليمنى عند التوقف.",
      "يتبادلان الضحك والنظر لبعضهما."
    ],
    "stepsEn": [
      "Groom raises his left hand above bride's head.",
      "Bride holds his hand and spins slowly underneath.",
      "Bride holds bouquet out with free hand.",
      "Groom steadies her waist mid-spin.",
      "Both laugh looking at each other."
    ],
    "photographerTips": {
      "angleAr": "منخفضة لإبراز طيران الفستان",
      "angleEn": "Low angle for skirt flare",
      "lensMm": "35mm",
      "distanceAr": "3 أمتار",
      "distanceEn": "3m",
      "lightingAr": "إضاءة خارجية أو غروب",
      "lightingEn": "Open shade or sunset",
      "compositionAr": "التقاط متتابع سريع",
      "compositionEn": "Continuous burst mode",
      "suggestedAperture": "f/2.8",
      "suggestedShutter": "1/1250s"
    },
    "propsAr": ["باقة زهور بيضاء"],
    "propsEn": ["White floral bouquet"],
    "commonMistakesAr": ["الدوران بسرعة مفرطة.", "رفع مرفق العريس أمام وجهه."],
    "commonMistakesEn": ["Spinning too fast.", "Blocking face with raised arm."],
    "directorCueAr": "ارفع يدك وأدرها ببطء دورة واحدة وكأنكما في رقصة هادئة، واضحكا معاً عند التوقف.",
    "directorCueEn": "Raise your hand and spin her slowly under your arm, then laugh together.",
    "illustrationSpec": {
      "framing": "Three-quarter dynamic portrait",
      "figuresPosition": "Groom spinning bride",
      "colorPalette": ["#2F343A", "#FFFFFF", "#C8C9CD", "#F2A7A7"],
      "backgroundTint": "SAGE"
    },
    "imageGenerationPrompt": "Flat vector groom spinning bride on #2F343A."
  },
  {
    "id": "pose_09",
    "assetName": "pose_09",
    "nameAr": "هدوء مقعد النافذة",
    "nameEn": "Window Seat Serenity",
    "shortDescriptionAr": "جلسة أنيقة للعروس منفردة تبرز تفاصيل ياقة الفستان والأكمام المنفوخة.",
    "shortDescriptionEn": "Graceful solo seated portrait highlighting the bodice and puff sleeves.",
    "category": "SITTING",
    "subject": "BRIDE_SOLO",
    "difficulty": "MEDIUM",
    "moodTags": ["EDITORIAL", "ROMANTIC"],
    "locationTags": ["INDOOR"],
    "bestForDressSilhouettesAr": ["أكمام منفوخة", "ياقة القلب"],
    "bestForDressSilhouettesEn": ["Puff Sleeves", "Sweetheart Neckline"],
    "stepsAr": [
      "تجلس العروس على طرف مقعد منخفض مع استقامة الظهر.",
      "تميل بركبتيها قليلاً نحو الجانب وترتب طيات الفستان.",
      "تضع الباقة على حجرها وتمسكها بكلتا يديها.",
      "تميل برأسها قليلاً نحو الكتف الأمامي.",
      "تنظر نحو ضوء النافذة بابتسامة هادئة."
    ],
    "stepsEn": [
      "Bride sits on front edge of a low seat with a tall back.",
      "Angles knees to one side and fans the white skirt.",
      "Rests the daisy bouquet gently on her lap.",
      "Tilts head slightly toward front shoulder.",
      "Gazes softly toward the window light."
    ],
    "photographerTips": {
      "angleAr": "مستوى عين العروس وهي جالسة",
      "angleEn": "Seated eye-level",
      "lensMm": "50mm",
      "distanceAr": "1.8 متر",
      "distanceEn": "1.8m",
      "lightingAr": "إضاءة نافذة جانبية كبيرة",
      "lightingEn": "Large side window light",
      "compositionAr": "تأطير عمودي متوازن",
      "compositionEn": "Balanced vertical framing",
      "suggestedAperture": "f/2.0",
      "suggestedShutter": "1/250s"
    },
    "propsAr": ["تاج زهور", "باقة أقحوان"],
    "propsEn": ["Floral crown", "Daisy bouquet"],
    "commonMistakesAr": ["الجلوس في عمق الكرسي وتقوس الظهر.", "إخفاء الرقبة بين الكتفين."],
    "commonMistakesEn": ["Slouching back into chair.", "Sinking neck."],
    "directorCueAr": "اجلسي على طرف المقعد بظهر مستقيم، ضعي الباقة في حجرك وانظري بهدوء نحو النافذة.",
    "directorCueEn": "Perch on the edge of the seat with a tall posture and look toward the window.",
    "illustrationSpec": {
      "framing": "Medium seated portrait",
      "figuresPosition": "Solo bride seated gracefully",
      "colorPalette": ["#2F343A", "#FFFFFF", "#FCE0D2", "#F2A7A7"],
      "backgroundTint": "MIST"
    },
    "imageGenerationPrompt": "Flat vector seated solo bride on #2F343A."
  },
  {
    "id": "pose_10",
    "assetName": "pose_10",
    "nameAr": "لمسة طية السترة والصديري",
    "nameEn": "Lapel Fix & Vest Detail",
    "shortDescriptionAr": "لقطة تفصيلية قريبة ليدي العروس وهما ترتبان طية سترة العريس الرمادية.",
    "shortDescriptionEn": "Close-up detail of bride's hands adjusting groom's light-gray jacket lapel.",
    "category": "CLOSE_UP",
    "subject": "DETAILS",
    "difficulty": "MEDIUM",
    "moodTags": ["EDITORIAL"],
    "locationTags": ["INDOOR", "STUDIO"],
    "bestForDressSilhouettesAr": ["أكمام منفوخة", "جميع القصات"],
    "bestForDressSilhouettesEn": ["Puff Sleeves", "All Silhouettes"],
    "stepsAr": [
      "يقف العروسان متقابلين بمسافة قريبة جداً.",
      "يضع العريس يده اليمنى في جيب البنطلون.",
      "ترفع العروس يدها لتمسك بطية سترة العريس الرمادية بلطف.",
      "تظهر تفاصيل الصديري المنقوش وربطة العنق الفضية في المنتصف.",
      "تبقى باقة الزهور ممسوكة باليد الأخرى أسفل الصدر."
    ],
    "stepsEn": [
      "Couple stands closely facing one another.",
      "Groom places his right hand into trouser pocket.",
      "Bride raises her hand to smooth groom's gray lapel.",
      "Patterned vest and silver tie remain centered.",
      "Bride holds daisy bouquet low with other hand."
    ],
    "photographerTips": {
      "angleAr": "مستوى الصدر",
      "angleEn": "Chest-level",
      "lensMm": "85mm",
      "distanceAr": "1 متر",
      "distanceEn": "1m",
      "lightingAr": "إضاءة ناعمة تبرز قماش البدلة",
      "lightingEn": "Soft light highlighting suit texture",
      "compositionAr": "خطوط قطرية بين ذراع العروس وطية السترة",
      "compositionEn": "Diagonal leading lines",
      "suggestedAperture": "f/2.8",
      "suggestedShutter": "1/320s"
    },
    "propsAr": ["بدلة رمادية ثلاثية بصديري منقوش", "باقة أقحوان"],
    "propsEn": ["Light-gray 3-piece suit", "Daisy bouquet"],
    "commonMistakesAr": ["تغطية اليد لربطة العنق.", "شد طية السترة بقوة."],
    "commonMistakesEn": ["Covering tie knot.", "Pulling lapel tightly."],
    "directorCueAr": "ضعي يدك بنعومة على طية سترته وكأنك ترتبينها له قبل الدخول إلى القاعة.",
    "directorCueEn": "Gently smooth his jacket lapel with your fingertips.",
    "illustrationSpec": {
      "framing": "Tight chest-and-hands detail crop",
      "figuresPosition": "Bride hand on groom gray lapel",
      "colorPalette": ["#2F343A", "#C8C9CD", "#FFFFFF", "#FCE0D2"],
      "backgroundTint": "SAND"
    },
    "imageGenerationPrompt": "Flat vector detail bride adjusting groom lapel on #2F343A."
  }
]
""",

    "app/src/main/java/com/kadr/poses/KadrApplication.kt": """package com.kadr.poses

import android.app.Application
import dagger.hilt.android.HiltAndroidApp
import timber.log.Timber

@HiltAndroidApp
class KadrApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        if (BuildConfig.DEBUG) {
            Timber.plant(Timber.DebugTree())
        }
    }
}
""",

    "app/src/main/java/com/kadr/poses/domain/DomainLayer.kt": """package com.kadr.poses.domain

import androidx.compose.runtime.Immutable
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map
import kotlinx.serialization.Serializable
import javax.inject.Inject

@Serializable enum class PoseCategory { STANDING, SITTING, WALKING, CLOSE_UP }
@Serializable enum class PoseSubject { BRIDE_SOLO, COUPLE, DETAILS }
@Serializable enum class PoseDifficulty { EASY, MEDIUM, ADVANCED }
@Serializable enum class PoseMood { ROMANTIC, PLAYFUL, EDITORIAL, CINEMATIC }
@Serializable enum class PoseLocation { INDOOR, OUTDOOR, STUDIO }
enum class PoseSortOption { RECOMMENDED, DIFFICULTY, ALPHABETICAL }
enum class ThemePreference { LIGHT, DARK, SYSTEM }

@Immutable
@Serializable
data class PhotographerTips(
    val angleAr: String,
    val angleEn: String,
    val lensMm: String,
    val distanceAr: String,
    val distanceEn: String,
    val lightingAr: String,
    val lightingEn: String,
    val compositionAr: String,
    val compositionEn: String,
    val suggestedAperture: String,
    val suggestedShutter: String
)

@Immutable
@Serializable
data class IllustrationSpec(
    val framing: String,
    val figuresPosition: String,
    val colorPalette: List<String>,
    val backgroundTint: String
)

@Immutable
data class Pose(
    val id: String,
    val assetName: String,
    val nameAr: String,
    val nameEn: String,
    val shortDescriptionAr: String,
    val shortDescriptionEn: String,
    val category: PoseCategory,
    val subject: PoseSubject,
    val difficulty: PoseDifficulty,
    val moodTags: List<PoseMood>,
    val locationTags: List<PoseLocation>,
    val bestForDressSilhouettesAr: List<String>,
    val bestForDressSilhouettesEn: List<String>,
    val stepsAr: List<String>,
    val stepsEn: List<String>,
    val photographerTips: PhotographerTips,
    val propsAr: List<String>,
    val propsEn: List<String>,
    val commonMistakesAr: List<String>,
    val commonMistakesEn: List<String>,
    val directorCueAr: String,
    val directorCueEn: String,
    val illustrationSpec: IllustrationSpec,
    val imageGenerationPrompt: String,
    val isFavorite: Boolean
) {
    fun localizedName(isArabic: Boolean) = if (isArabic) nameAr else nameEn
    fun localizedDescription(isArabic: Boolean) = if (isArabic) shortDescriptionAr else shortDescriptionEn
    fun localizedDirectorCue(isArabic: Boolean) = if (isArabic) directorCueAr else directorCueEn
    fun localizedSteps(isArabic: Boolean) = if (isArabic) stepsAr else stepsEn
    fun localizedMistakes(isArabic: Boolean) = if (isArabic) commonMistakesAr else commonMistakesEn
    fun localizedSilhouettes(isArabic: Boolean) = if (isArabic) bestForDressSilhouettesAr else bestForDressSilhouettesEn
    fun localizedProps(isArabic: Boolean) = if (isArabic) propsAr else propsEn
}

@Immutable
data class ShotListEntry(
    val entryId: Long,
    val listId: Long,
    val pose: Pose,
    val sortOrder: Int,
    val isCompleted: Boolean
)

@Immutable
data class ShotListWithEntries(
    val id: Long,
    val title: String,
    val createdAt: Long,
    val entries: List<ShotListEntry>
) {
    val completedCount: Int get() = entries.count { it.isCompleted }
    val totalCount: Int get() = entries.size
}

@Immutable
data class PoseFilterState(
    val query: String = "",
    val selectedSubject: PoseSubject? = null,
    val selectedLocation: PoseLocation? = null,
    val selectedMood: PoseMood? = null,
    val selectedDifficulty: PoseDifficulty? = null,
    val sortOption: PoseSortOption = PoseSortOption.RECOMMENDED
)

@Immutable
data class AppSettings(
    val onboardingCompleted: Boolean = false,
    val themePreference: ThemePreference = ThemePreference.LIGHT,
    val languageTag: String = "ar"
)

interface PoseRepository {
    fun observeAllPoses(): Flow<List<Pose>>
    fun observeFavoritePoses(): Flow<List<Pose>>
    fun observePoseById(poseId: String): Flow<Pose?>
    suspend fun toggleFavorite(poseId: String)
    suspend fun ensureSeedLoaded()
}

interface ShotListRepository {
    fun observeAllShotLists(): Flow<List<ShotListWithEntries>>
    suspend fun createShotList(title: String): Long
    suspend fun deleteShotList(listId: Long)
    suspend fun addPoseToShotList(listId: Long, poseId: String)
    suspend fun removeEntryFromShotList(entryId: Long)
    suspend fun toggleEntryCompleted(entryId: Long, completed: Boolean)
    suspend fun moveEntryOrder(listId: Long, fromIndex: Int, toIndex: Int)
}

interface SettingsRepository {
    val settingsFlow: Flow<AppSettings>
    suspend fun setOnboardingCompleted(completed: Boolean)
    suspend fun setThemePreference(preference: ThemePreference)
    suspend fun setLanguageTag(tag: String)
}

class GetFilteredPosesUseCase @Inject constructor(
    private val poseRepository: PoseRepository
) {
    operator fun invoke(filter: PoseFilterState, isArabic: Boolean): Flow<List<Pose>> =
        poseRepository.observeAllPoses().map { poses ->
            val filtered = poses.filter { pose ->
                val q = filter.query.trim().lowercase()
                val matchesQuery = q.isEmpty() ||
                    pose.nameAr.lowercase().contains(q) ||
                    pose.nameEn.lowercase().contains(q) ||
                    pose.photographerTips.lensMm.lowercase().contains(q)
                val matchesSubject = filter.selectedSubject == null || pose.subject == filter.selectedSubject
                val matchesLocation = filter.selectedLocation == null || pose.locationTags.contains(filter.selectedLocation)
                val matchesMood = filter.selectedMood == null || pose.moodTags.contains(filter.selectedMood)
                val matchesDiff = filter.selectedDifficulty == null || pose.difficulty == filter.selectedDifficulty
                matchesQuery && matchesSubject && matchesLocation && matchesMood && matchesDiff
            }
            when (filter.sortOption) {
                PoseSortOption.RECOMMENDED -> filtered
                PoseSortOption.DIFFICULTY -> filtered.sortedBy { it.difficulty.ordinal }
                PoseSortOption.ALPHABETICAL -> filtered.sortedBy { it.localizedName(isArabic) }
            }
        }
}
""",

    "app/src/main/java/com/kadr/poses/data/DataLayer.kt": """package com.kadr.poses.data

import android.content.Context
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import androidx.room.*
import com.kadr.poses.domain.*
import dagger.hilt.android.qualifiers.ApplicationContext
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.withContext
import kotlinx.serialization.Serializable
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import timber.log.Timber
import javax.inject.Inject
import javax.inject.Singleton

@Serializable
data class PoseSeedDto(
    val id: String,
    val assetName: String,
    val nameAr: String,
    val nameEn: String,
    val shortDescriptionAr: String,
    val shortDescriptionEn: String,
    val category: PoseCategory,
    val subject: PoseSubject,
    val difficulty: PoseDifficulty,
    val moodTags: List<PoseMood>,
    val locationTags: List<PoseLocation>,
    val bestForDressSilhouettesAr: List<String>,
    val bestForDressSilhouettesEn: List<String>,
    val stepsAr: List<String>,
    val stepsEn: List<String>,
    val photographerTips: PhotographerTips,
    val propsAr: List<String>,
    val propsEn: List<String>,
    val commonMistakesAr: List<String>,
    val commonMistakesEn: List<String>,
    val directorCueAr: String,
    val directorCueEn: String,
    val illustrationSpec: IllustrationSpec,
    val imageGenerationPrompt: String
) {
    fun toEntity(fav: Boolean) = PoseEntity(
        id, assetName, nameAr, nameEn, shortDescriptionAr, shortDescriptionEn,
        category, subject, difficulty, moodTags, locationTags,
        bestForDressSilhouettesAr, bestForDressSilhouettesEn, stepsAr, stepsEn,
        photographerTips, propsAr, propsEn, commonMistakesAr, commonMistakesEn,
        directorCueAr, directorCueEn, illustrationSpec, imageGenerationPrompt, fav
    )
}

@Entity(tableName = "poses")
data class PoseEntity(
    @PrimaryKey val id: String,
    val assetName: String,
    val nameAr: String,
    val nameEn: String,
    val shortDescriptionAr: String,
    val shortDescriptionEn: String,
    val category: PoseCategory,
    val subject: PoseSubject,
    val difficulty: PoseDifficulty,
    val moodTags: List<PoseMood>,
    val locationTags: List<PoseLocation>,
    val bestForDressSilhouettesAr: List<String>,
    val bestForDressSilhouettesEn: List<String>,
    val stepsAr: List<String>,
    val stepsEn: List<String>,
    val photographerTips: PhotographerTips,
    val propsAr: List<String>,
    val propsEn: List<String>,
    val commonMistakesAr: List<String>,
    val commonMistakesEn: List<String>,
    val directorCueAr: String,
    val directorCueEn: String,
    val illustrationSpec: IllustrationSpec,
    val imageGenerationPrompt: String,
    val isFavorite: Boolean
) {
    fun toDomain() = Pose(
        id, assetName, nameAr, nameEn, shortDescriptionAr, shortDescriptionEn,
        category, subject, difficulty, moodTags, locationTags,
        bestForDressSilhouettesAr, bestForDressSilhouettesEn, stepsAr, stepsEn,
        photographerTips, propsAr, propsEn, commonMistakesAr, commonMistakesEn,
        directorCueAr, directorCueEn, illustrationSpec, imageGenerationPrompt, isFavorite
    )
}

@Entity(tableName = "shot_lists")
data class ShotListEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val title: String,
    val createdAt: Long
)

@Entity(tableName = "shot_list_entries")
data class ShotListEntryEntity(
    @PrimaryKey(autoGenerate = true) val entryId: Long = 0,
    val listId: Long,
    val poseId: String,
    val sortOrder: Int,
    val isCompleted: Boolean = false
)

class KadrTypeConverters {
    private val json = Json { ignoreUnknownKeys = true }
    @TypeConverter fun fromStrList(v: List<String>) = json.encodeToString(v)
    @TypeConverter fun toStrList(v: String): List<String> = json.decodeFromString(v)
    @TypeConverter fun fromMoods(v: List<PoseMood>) = json.encodeToString(v)
    @TypeConverter fun toMoods(v: String): List<PoseMood> = json.decodeFromString(v)
    @TypeConverter fun fromLocs(v: List<PoseLocation>) = json.encodeToString(v)
    @TypeConverter fun toLocs(v: String): List<PoseLocation> = json.decodeFromString(v)
    @TypeConverter fun fromTips(v: PhotographerTips) = json.encodeToString(v)
    @TypeConverter fun toTips(v: String): PhotographerTips = json.decodeFromString(v)
    @TypeConverter fun fromSpec(v: IllustrationSpec) = json.encodeToString(v)
    @TypeConverter fun toSpec(v: String): IllustrationSpec = json.decodeFromString(v)
}

@Dao
interface PoseDao {
    @Query("SELECT * FROM poses ORDER BY id ASC") fun observeAllPoses(): Flow<List<PoseEntity>>
    @Query("SELECT * FROM poses WHERE isFavorite = 1 ORDER BY id ASC") fun observeFavoritePoses(): Flow<List<PoseEntity>>
    @Query("SELECT * FROM poses WHERE id = :id LIMIT 1") fun observePoseById(id: String): Flow<PoseEntity?>
    @Query("SELECT * FROM poses WHERE id = :id LIMIT 1") suspend fun getPoseByIdOnce(id: String): PoseEntity?
    @Query("SELECT COUNT(*) FROM poses") suspend fun getPoseCount(): Int
    @Insert(onConflict = OnConflictStrategy.REPLACE) suspend fun upsertPoses(poses: List<PoseEntity>)
    @Query("UPDATE poses SET isFavorite = :fav WHERE id = :id") suspend fun updateFavorite(id: String, fav: Boolean)
}

@Dao
interface ShotListDao {
    @Query("SELECT * FROM shot_lists ORDER BY createdAt DESC") fun observeAllLists(): Flow<List<ShotListEntity>>
    @Query("SELECT * FROM shot_list_entries ORDER BY sortOrder ASC") fun observeAllEntries(): Flow<List<ShotListEntryEntity>>
    @Query("SELECT * FROM shot_list_entries WHERE listId = :listId ORDER BY sortOrder ASC")
    suspend fun getEntriesForListOnce(listId: Long): List<ShotListEntryEntity>
    @Insert(onConflict = OnConflictStrategy.REPLACE) suspend fun insertShotList(list: ShotListEntity): Long
    @Query("DELETE FROM shot_lists WHERE id = :listId") suspend fun deleteShotList(listId: Long)
    @Insert(onConflict = OnConflictStrategy.REPLACE) suspend fun insertEntry(entry: ShotListEntryEntity): Long
    @Query("DELETE FROM shot_list_entries WHERE entryId = :entryId") suspend fun deleteEntry(entryId: Long)
    @Query("UPDATE shot_list_entries SET isCompleted = :done WHERE entryId = :entryId")
    suspend fun updateEntryCompleted(entryId: Long, done: Boolean)
    @Query("UPDATE shot_list_entries SET sortOrder = :order WHERE entryId = :entryId")
    suspend fun updateEntrySortOrder(entryId: Long, order: Int)
}

@Database(entities = [PoseEntity::class, ShotListEntity::class, ShotListEntryEntity::class], version = 1, exportSchema = false)
@TypeConverters(KadrTypeConverters::class)
abstract class KadrDatabase : RoomDatabase() {
    abstract fun poseDao(): PoseDao
    abstract fun shotListDao(): ShotListDao
}

private val Context.dataStore by preferencesDataStore(name = "kadr_settings")

@Singleton
class PoseRepositoryImpl @Inject constructor(
    @ApplicationContext private val context: Context,
    private val poseDao: PoseDao,
    private val shotListDao: ShotListDao,
    private val json: Json
) : PoseRepository {
    override fun observeAllPoses() = poseDao.observeAllPoses().map { it.map(PoseEntity::toDomain) }
    override fun observeFavoritePoses() = poseDao.observeFavoritePoses().map { it.map(PoseEntity::toDomain) }
    override fun observePoseById(poseId: String) = poseDao.observePoseById(poseId).map { it?.toDomain() }

    override suspend fun toggleFavorite(poseId: String) {
        val current = poseDao.getPoseByIdOnce(poseId) ?: return
        poseDao.updateFavorite(poseId, !current.isFavorite)
    }

    override suspend fun ensureSeedLoaded() = withContext(Dispatchers.IO) {
        runCatching {
            val count = poseDao.getPoseCount()
            val raw = context.assets.open("poses_seed.json").bufferedReader().use { it.readText() }
            val dtos = json.decodeFromString<List<PoseSeedDto>>(raw)
            if (count < dtos.size) {
                val entities = dtos.map { dto ->
                    dto.toEntity(poseDao.getPoseByIdOnce(dto.id)?.isFavorite ?: false)
                }
                poseDao.upsertPoses(entities)
                if (count == 0 && entities.isNotEmpty()) {
                    val listId = shotListDao.insertShotList(
                        ShotListEntity(title = "جلسة الساعة الذهبية • Golden Hour", createdAt = System.currentTimeMillis())
                    )
                    entities.take(4).forEachIndexed { idx, p ->
                        shotListDao.insertEntry(ShotListEntryEntity(listId = listId, poseId = p.id, sortOrder = idx))
                    }
                }
            }
        }.onFailure { Timber.e(it, "Failed to seed database") }
        Unit
    }
}

@Singleton
class ShotListRepositoryImpl @Inject constructor(
    private val shotListDao: ShotListDao,
    private val poseDao: PoseDao
) : ShotListRepository {
    override fun observeAllShotLists(): Flow<List<ShotListWithEntries>> = combine(
        shotListDao.observeAllLists(),
        shotListDao.observeAllEntries(),
        poseDao.observeAllPoses()
    ) { lists, entries, poses ->
        val map = poses.associateBy({ it.id }, { it.toDomain() })
        lists.map { list ->
            val listEntries = entries.filter { it.listId == list.id }.sortedBy { it.sortOrder }.mapNotNull { e ->
                map[e.poseId]?.let { p -> ShotListEntry(e.entryId, e.listId, p, e.sortOrder, e.isCompleted) }
            }
            ShotListWithEntries(list.id, list.title, list.createdAt, listEntries)
        }
    }

    override suspend fun createShotList(title: String) =
        shotListDao.insertShotList(ShotListEntity(title = title.trim(), createdAt = System.currentTimeMillis()))

    override suspend fun deleteShotList(listId: Long) = shotListDao.deleteShotList(listId)

    override suspend fun addPoseToShotList(listId: Long, poseId: String) {
        val current = shotListDao.getEntriesForListOnce(listId)
        if (current.any { it.poseId == poseId }) return
        shotListDao.insertEntry(ShotListEntryEntity(listId = listId, poseId = poseId, sortOrder = current.size))
    }

    override suspend fun removeEntryFromShotList(entryId: Long) = shotListDao.deleteEntry(entryId)
    override suspend fun toggleEntryCompleted(entryId: Long, completed: Boolean) =
        shotListDao.updateEntryCompleted(entryId, completed)

    override suspend fun moveEntryOrder(listId: Long, fromIndex: Int, toIndex: Int) {
        val list = shotListDao.getEntriesForListOnce(listId).toMutableList()
        if (fromIndex !in list.indices || toIndex !in list.indices) return
        val item = list.removeAt(fromIndex)
        list.add(toIndex, item)
        list.forEachIndexed { idx, entry -> shotListDao.updateEntrySortOrder(entry.entryId, idx) }
    }
}

@Singleton
class SettingsRepositoryImpl @Inject constructor(
    @ApplicationContext private val context: Context
) : SettingsRepository {
    private val keyOnboard = booleanPreferencesKey("onboarding_completed")
    private val keyTheme = stringPreferencesKey("theme_pref")
    private val keyLang = stringPreferencesKey("language_tag")

    override val settingsFlow: Flow<AppSettings> = context.dataStore.data.map { prefs ->
        val theme = runCatching { ThemePreference.valueOf(prefs[keyTheme] ?: "LIGHT") }.getOrDefault(ThemePreference.LIGHT)
        AppSettings(
            onboardingCompleted = prefs[keyOnboard] ?: false,
            themePreference = theme,
            languageTag = prefs[keyLang] ?: "ar"
        )
    }

    override suspend fun setOnboardingCompleted(completed: Boolean) {
        context.dataStore.edit { it[keyOnboard] = completed }
    }

    override suspend fun setThemePreference(preference: ThemePreference) {
        context.dataStore.edit { it[keyTheme] = preference.name }
    }

    override suspend fun setLanguageTag(tag: String) {
        context.dataStore.edit { it[keyLang] = tag }
    }
}
""",

    "app/src/main/java/com/kadr/poses/di/AppModule.kt": """package com.kadr.poses.di

import android.content.Context
import androidx.room.Room
import com.kadr.poses.data.*
import com.kadr.poses.domain.*
import dagger.Binds
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import kotlinx.serialization.json.Json
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object DatabaseModule {
    @Provides @Singleton
    fun provideJson(): Json = Json { ignoreUnknownKeys = true; isLenient = true }

    @Provides @Singleton
    fun provideDatabase(@ApplicationContext context: Context): KadrDatabase =
        Room.databaseBuilder(context, KadrDatabase::class.java, "kadr_poses.db")
            .fallbackToDestructiveMigration().build()

    @Provides fun providePoseDao(db: KadrDatabase): PoseDao = db.poseDao()
    @Provides fun provideShotListDao(db: KadrDatabase): ShotListDao = db.shotListDao()
}

@Module
@InstallIn(SingletonComponent::class)
abstract class RepositoryModule {
    @Binds @Singleton abstract fun bindPoseRepo(impl: PoseRepositoryImpl): PoseRepository
    @Binds @Singleton abstract fun bindShotListRepo(impl: ShotListRepositoryImpl): ShotListRepository
    @Binds @Singleton abstract fun bindSettingsRepo(impl: SettingsRepositoryImpl): SettingsRepository
}
""",

    "app/src/main/java/com/kadr/poses/ui/theme/ThemeLayer.kt": """package com.kadr.poses.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

val WarmIvory = Color(0xFFFBF8F4)
val PureWhite = Color(0xFFFFFFFF)
val CharcoalInk = Color(0xFF2F343A)
val DeepCharcoal = Color(0xFF181B1E)
val DarkSurface = Color(0xFF22262B)
val BlushRoseReference = Color(0xFFF2A7A7)
val DeepRosePrimary = Color(0xFF8F3B3B)
val DeepRoseContainer = Color(0xFFFCE4E4)
val OnDeepRoseContainer = Color(0xFF3B0D0D)
val DarkRoseContainer = Color(0xFF5C2222)
val SageSecondary = Color(0xFF4F6854)
val SageSecondaryDark = Color(0xFFB4CCB8)
val SageContainerLight = Color(0xFFDCE8DE)
val OnSageContainerLight = Color(0xFF132617)
val SageContainerDark = Color(0xFF374E3C)
val WarmSurfaceVariant = Color(0xFFF2ECE4)
val OnWarmSurfaceVariant = Color(0xFF4F4944)

val FrameTintBlushLight = Color(0xFFFBE3E0)
val FrameTintSageLight = Color(0xFFE3EDE1)
val FrameTintSandLight = Color(0xFFF3E9DC)
val FrameTintMistLight = Color(0xFFE6EAF2)

val FrameTintBlushDark = Color(0xFF3A2929)
val FrameTintSageDark = Color(0xFF263328)
val FrameTintSandDark = Color(0xFF352F26)
val FrameTintMistDark = Color(0xFF272C36)

val SkinBaseTone = Color(0xFFFCE0D2)
val GroomSuitGray = Color(0xFFC8C9CD)
val GroomSuitShadow = Color(0xFFA6ABB2)
val OutlineBlack = Color(0xFF0D0D0D)

@Immutable
data class KadrExtendedColors(
    val charcoalBackdrop: Color = CharcoalInk,
    val blushCheekAccent: Color = BlushRoseReference,
    val tintBlush: Color = FrameTintBlushLight,
    val tintSage: Color = FrameTintSageLight,
    val tintSand: Color = FrameTintSandLight,
    val tintMist: Color = FrameTintMistLight
)

@Immutable
data class KadrDimens(
    val grid0_5: Dp = 4.dp,
    val grid1: Dp = 8.dp,
    val grid1_5: Dp = 12.dp,
    val grid2: Dp = 16.dp,
    val screenMargin: Dp = 20.dp,
    val grid3: Dp = 24.dp,
    val grid4: Dp = 32.dp,
    val grid6: Dp = 48.dp,
    val minTouchTarget: Dp = 48.dp,
    val tonalElevationLow: Dp = 2.dp,
    val tonalElevationMedium: Dp = 4.dp,
    val poseGridCardHeight: Dp = 250.dp,
    val detailHeroHeight: Dp = 340.dp
)

val LocalKadrColors = staticCompositionLocalOf { KadrExtendedColors() }
val LocalKadrDimens = staticCompositionLocalOf { KadrDimens() }

private val LightColors = lightColorScheme(
    primary = DeepRosePrimary,
    onPrimary = PureWhite,
    primaryContainer = DeepRoseContainer,
    onPrimaryContainer = OnDeepRoseContainer,
    secondary = SageSecondary,
    onSecondary = PureWhite,
    secondaryContainer = SageContainerLight,
    onSecondaryContainer = OnSageContainerLight,
    background = WarmIvory,
    onBackground = CharcoalInk,
    surface = PureWhite,
    onSurface = CharcoalInk,
    surfaceVariant = WarmSurfaceVariant,
    onSurfaceVariant = OnWarmSurfaceVariant
)

private val DarkColors = darkColorScheme(
    primary = BlushRoseReference,
    onPrimary = CharcoalInk,
    primaryContainer = DarkRoseContainer,
    onPrimaryContainer = DeepRoseContainer,
    secondary = SageSecondaryDark,
    onSecondary = CharcoalInk,
    secondaryContainer = SageContainerDark,
    onSecondaryContainer = SageContainerLight,
    background = DeepCharcoal,
    onBackground = WarmIvory,
    surface = DarkSurface,
    onSurface = WarmIvory,
    surfaceVariant = CharcoalInk,
    onSurfaceVariant = WarmIvory
)

val KadrShapes = Shapes(
    extraSmall = RoundedCornerShape(8.dp),
    small = RoundedCornerShape(50),
    medium = RoundedCornerShape(16.dp),
    large = RoundedCornerShape(24.dp),
    extraLarge = RoundedCornerShape(32.dp)
)

@Composable
fun KadrTheme(darkTheme: Boolean = isSystemInDarkTheme(), content: @Composable () -> Unit) {
    val ext = if (darkTheme) {
        KadrExtendedColors(
            tintBlush = FrameTintBlushDark,
            tintSage = FrameTintSageDark,
            tintSand = FrameTintSandDark,
            tintMist = FrameTintMistDark
        )
    } else KadrExtendedColors()

    CompositionLocalProvider(LocalKadrColors provides ext, LocalKadrDimens provides KadrDimens()) {
        MaterialTheme(
            colorScheme = if (darkTheme) DarkColors else LightColors,
            shapes = KadrShapes,
            content = content
        )
    }
}

object KadrThemeTokens {
    val colors: KadrExtendedColors @Composable @ReadOnlyComposable get() = LocalKadrColors.current
    val dimens: KadrDimens @Composable @ReadOnlyComposable get() = LocalKadrDimens.current
}
""",

    "app/src/main/java/com/kadr/poses/ui/components/CoreComponents.kt": """package com.kadr.poses.ui.components

import androidx.compose.animation.core.animateFloatAsState
import androidx.compose.animation.core.spring
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.Canvas
import androidx.compose.foundation.background
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.interaction.collectIsPressedAsState
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.outlined.FavoriteBorder
import androidx.compose.material.icons.outlined.RecordVoiceOver
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.geometry.CornerRadius
import androidx.compose.ui.geometry.Offset
import androidx.compose.ui.geometry.Size
import androidx.compose.ui.graphics.Path
import androidx.compose.ui.graphics.StrokeCap
import androidx.compose.ui.graphics.StrokeJoin
import androidx.compose.ui.graphics.drawscope.Stroke
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextOverflow
import androidx.compose.ui.unit.dp
import coil.compose.AsyncImage
import coil.request.ImageRequest
import com.kadr.poses.ui.theme.*

enum class IllustrationFrameTint { CHARCOAL_STUDIO, BLUSH, SAGE, SAND, MIST }

@Immutable
data class PoseCardUiModel(
    val id: String,
    val title: String,
    val subjectLabel: String,
    val difficultyLabel: String,
    val assetName: String,
    val frameTint: IllustrationFrameTint,
    val isFavorite: Boolean
)

@Composable
fun PoseIllustrationCanvas(
    assetName: String,
    contentDesc: String,
    frameTint: IllustrationFrameTint,
    modifier: Modifier = Modifier
) {
    val ext = KadrThemeTokens.colors
    val bg = when (frameTint) {
        IllustrationFrameTint.CHARCOAL_STUDIO -> ext.charcoalBackdrop
        IllustrationFrameTint.BLUSH -> ext.tintBlush
        IllustrationFrameTint.SAGE -> ext.tintSage
        IllustrationFrameTint.SAND -> ext.tintSand
        IllustrationFrameTint.MIST -> ext.tintMist
    }
    var loadFailed by remember(assetName) { mutableStateOf(false) }
    val context = LocalContext.current

    Box(
        modifier = modifier.background(bg).semantics { contentDescription = contentDesc },
        contentAlignment = Alignment.Center
    ) {
        if (!loadFailed) {
            AsyncImage(
                model = ImageRequest.Builder(context)
                    .data("file:///android_asset/illustrations/$assetName.webp")
                    .crossfade(true)
                    .build(),
                contentDescription = null,
                contentScale = ContentScale.Fit,
                onError = { loadFailed = true },
                modifier = Modifier.fillMaxSize()
            )
        } else {
            StyleBibleVectorIllustration(
                poseSeed = assetName.hashCode(),
                isDarkBackdrop = frameTint == IllustrationFrameTint.CHARCOAL_STUDIO,
                modifier = Modifier.fillMaxSize()
            )
        }
    }
}

@Composable
private fun StyleBibleVectorIllustration(
    poseSeed: Int,
    isDarkBackdrop: Boolean,
    modifier: Modifier = Modifier
) {
    Canvas(modifier = modifier) {
        val w = size.width
        val h = size.height
        val strokeBold = Stroke(width = (w * 0.015f).coerceAtLeast(3.5f), cap = StrokeCap.Round, join = StrokeJoin.Round)
        val strokeThin = Stroke(width = (w * 0.008f).coerceAtLeast(2f), cap = StrokeCap.Round)
        val shift = ((poseSeed % 3) - 1) * (w * 0.015f)

        val groomX = w * 0.39f + shift
        val groomTop = h * 0.45f
        drawRoundRect(GroomSuitGray, Offset(groomX - w * 0.16f, groomTop), Size(w * 0.30f, h * 0.55f), CornerRadius(w * 0.08f))
        drawRoundRect(GroomSuitShadow, Offset(groomX - w * 0.02f, groomTop + h * 0.04f), Size(w * 0.12f, h * 0.48f), CornerRadius(w * 0.04f))
        drawRoundRect(OutlineBlack, Offset(groomX - w * 0.16f, groomTop), Size(w * 0.30f, h * 0.55f), CornerRadius(w * 0.08f), style = strokeBold)

        val groomHead = Offset(groomX + w * 0.02f, h * 0.33f)
        val r = w * 0.095f
        drawCircle(SkinBaseTone, r, groomHead)
        drawCircle(OutlineBlack, r, groomHead, style = strokeBold)
        drawArc(OutlineBlack, 150f, 190f, true, Offset(groomHead.x - r * 1.05f, groomHead.y - r * 1.08f), Size(r * 2.1f, r * 1.4f))
        drawCircle(BlushRoseReference, r * 0.22f, Offset(groomHead.x + r * 0.45f, groomHead.y + r * 0.15f))

        val brideX = w * 0.61f - shift
        val brideTop = h * 0.48f
        drawCircle(OutlineBlack, r * 1.25f, Offset(brideX, h * 0.38f))
        val gown = Path().apply {
            moveTo(brideX - w * 0.12f, brideTop)
            lineTo(brideX + w * 0.12f, brideTop)
            lineTo(brideX + w * 0.22f, h)
            lineTo(brideX - w * 0.20f, h)
            close()
        }
        drawPath(gown, PureWhite)
        drawPath(gown, OutlineBlack, style = strokeBold)

        val sleeve = Offset(brideX + w * 0.11f, brideTop + h * 0.05f)
        drawCircle(PureWhite, w * 0.075f, sleeve)
        drawCircle(OutlineBlack, w * 0.075f, sleeve, style = strokeBold)

        val brideHead = Offset(brideX - w * 0.01f, h * 0.35f)
        drawCircle(SkinBaseTone, r * 0.92f, brideHead)
        drawCircle(OutlineBlack, r * 0.92f, brideHead, style = strokeBold)
        drawCircle(BlushRoseReference, r * 0.22f, Offset(brideHead.x + r * 0.25f, brideHead.y + r * 0.12f))
        drawCircle(BlushRoseReference, r * 0.18f, Offset(brideHead.x - r * 0.45f, brideHead.y + r * 0.08f))

        for (i in -3..3) {
            drawCircle(PureWhite, w * 0.012f, Offset(brideHead.x + i * (w * 0.022f), brideHead.y - r * 0.88f + (i * i * 1.5f)))
        }

        val hc = Offset(groomHead.x - r * 0.9f, groomHead.y - r * 1.15f)
        val hs = w * 0.045f
        val heart = Path().apply {
            moveTo(hc.x, hc.y + hs * 0.35f)
            cubicTo(hc.x - hs * 0.8f, hc.y - hs * 0.2f, hc.x - hs * 0.4f, hc.y - hs * 0.9f, hc.x, hc.y - hs * 0.35f)
            cubicTo(hc.x + hs * 0.4f, hc.y - hs * 0.9f, hc.x + hs * 0.8f, hc.y - hs * 0.2f, hc.x, hc.y + hs * 0.35f)
        }
        drawPath(heart, if (isDarkBackdrop) PureWhite else OutlineBlack, style = strokeThin)
    }
}

@Composable
fun PoseCard(
    model: PoseCardUiModel,
    favoriteActionContentDesc: String,
    onCardClick: (String) -> Unit,
    onFavoriteToggle: (String) -> Unit,
    modifier: Modifier = Modifier
) {
    val dimens = KadrThemeTokens.dimens
    val haptic = LocalHapticFeedback.current
    val interactionSource = remember { MutableInteractionSource() }
    val isPressed by interactionSource.collectIsPressedAsState()
    val scale by animateFloatAsState(if (isPressed) 0.97f else 1f, spring(0.75f, 400f), label = "scale")

    Card(
        onClick = { onCardClick(model.id) },
        interactionSource = interactionSource,
        shape = MaterialTheme.shapes.large,
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.surface),
        elevation = CardDefaults.cardElevation(defaultElevation = dimens.tonalElevationLow),
        modifier = modifier.graphicsLayer { scaleX = scale; scaleY = scale }
    ) {
        Column(modifier = Modifier.fillMaxWidth()) {
            Box(
                modifier = Modifier
                    .fillMaxWidth()
                    .height(dimens.poseGridCardHeight * 0.7f)
                    .padding(dimens.grid1)
                    .clip(MaterialTheme.shapes.medium)
            ) {
                PoseIllustrationCanvas(model.assetName, model.title, model.frameTint, Modifier.fillMaxSize())
                Surface(
                    shape = CircleShape,
                    color = MaterialTheme.colorScheme.surface.copy(alpha = 0.88f),
                    modifier = Modifier.align(Alignment.TopEnd).padding(dimens.grid1).size(dimens.minTouchTarget)
                ) {
                    IconButton(onClick = {
                        haptic.performHapticFeedback(HapticFeedbackType.LongPress)
                        onFavoriteToggle(model.id)
                    }) {
                        Icon(
                            imageVector = if (model.isFavorite) Icons.Filled.Favorite else Icons.Outlined.FavoriteBorder,
                            contentDescription = favoriteActionContentDesc,
                            tint = if (model.isFavorite) MaterialTheme.colorScheme.primary else MaterialTheme.colorScheme.onSurface
                        )
                    }
                }
            }
            Column(modifier = Modifier.padding(horizontal = dimens.grid2, vertical = dimens.grid1)) {
                Text(model.title, style = MaterialTheme.typography.titleMedium, maxLines = 1, overflow = TextOverflow.Ellipsis)
                Text("${model.subjectLabel} • ${model.difficultyLabel}", style = MaterialTheme.typography.labelMedium, color = MaterialTheme.colorScheme.secondary)
            }
        }
    }
}

@Composable
fun DirectorCueBanner(label: String, cueText: String, modifier: Modifier = Modifier) {
    val dimens = KadrThemeTokens.dimens
    Surface(
        shape = MaterialTheme.shapes.large,
        color = MaterialTheme.colorScheme.primaryContainer.copy(alpha = 0.55f),
        border = BorderStroke(1.dp, MaterialTheme.colorScheme.primary.copy(alpha = 0.25f)),
        modifier = modifier.fillMaxWidth()
    ) {
        Column(modifier = Modifier.padding(dimens.grid2)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Icon(Icons.Outlined.RecordVoiceOver, null, tint = MaterialTheme.colorScheme.primary)
                Spacer(Modifier.width(dimens.grid1))
                Text(label, style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.primary)
            }
            Spacer(Modifier.height(dimens.grid1))
            Text("“$cueText”", style = MaterialTheme.typography.titleMedium)
        }
    }
}

@Composable
fun KadrFilterChip(label: String, selected: Boolean, onClick: () -> Unit, modifier: Modifier = Modifier) {
    FilterChip(
        selected = selected,
        onClick = onClick,
        label = { Text(label) },
        leadingIcon = if (selected) { { Icon(Icons.Filled.Check, null) } } else null,
        shape = MaterialTheme.shapes.small,
        modifier = modifier.defaultMinSize(minHeight = KadrThemeTokens.dimens.minTouchTarget)
    )
}

@Composable
fun EmptyStateView(
    title: String,
    subtitle: String,
    actionLabel: String? = null,
    onActionClick: (() -> Unit)? = null,
    modifier: Modifier = Modifier
) {
    val dimens = KadrThemeTokens.dimens
    Column(
        modifier = modifier.fillMaxWidth().padding(dimens.grid4),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        PoseIllustrationCanvas("empty", title, IllustrationFrameTint.BLUSH, Modifier.size(120.dp).clip(CircleShape))
        Spacer(Modifier.height(dimens.grid2))
        Text(title, style = MaterialTheme.typography.headlineSmall, textAlign = TextAlign.Center)
        Spacer(Modifier.height(dimens.grid1))
        Text(subtitle, style = MaterialTheme.typography.bodyMedium, textAlign = TextAlign.Center)
        if (actionLabel != null && onActionClick != null) {
            Spacer(Modifier.height(dimens.grid2))
            Button(onClick = onActionClick) { Text(actionLabel) }
        }
    }
}
""",

    "app/src/main/java/com/kadr/poses/ui/screens/ScreensLayer.kt": """package com.kadr.poses.ui.screens

import android.content.Intent
import androidx.appcompat.app.AppCompatDelegate
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.pager.HorizontalPager
import androidx.compose.foundation.pager.rememberPagerState
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.selection.selectable
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.outlined.ArrowBack
import androidx.compose.material.icons.filled.Favorite
import androidx.compose.material.icons.outlined.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalView
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.core.os.LocaleListCompat
import androidx.lifecycle.ViewModel
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewModelScope
import com.kadr.poses.R
import com.kadr.poses.domain.*
import com.kadr.poses.ui.components.*
import com.kadr.poses.ui.theme.CharcoalInk
import com.kadr.poses.ui.theme.KadrThemeTokens
import com.kadr.poses.ui.theme.PureWhite
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.launch
import javax.inject.Inject

@Composable
fun Pose.toCardUiModel(isArabic: Boolean): PoseCardUiModel {
    val tint = runCatching { IllustrationFrameTint.valueOf(illustrationSpec.backgroundTint) }
        .getOrDefault(IllustrationFrameTint.BLUSH)
    return PoseCardUiModel(
        id = id,
        title = localizedName(isArabic),
        subjectLabel = subject.localizedLabel(),
        difficultyLabel = difficulty.localizedLabel(),
        assetName = assetName,
        frameTint = tint,
        isFavorite = isFavorite
    )
}

@Composable fun PoseSubject.localizedLabel() = when (this) {
    PoseSubject.BRIDE_SOLO -> stringResource(R.string.subject_bride_solo)
    PoseSubject.COUPLE -> stringResource(R.string.subject_couple)
    PoseSubject.DETAILS -> stringResource(R.string.subject_details)
}

@Composable fun PoseDifficulty.localizedLabel() = when (this) {
    PoseDifficulty.EASY -> stringResource(R.string.difficulty_easy)
    PoseDifficulty.MEDIUM -> stringResource(R.string.difficulty_medium)
    PoseDifficulty.ADVANCED -> stringResource(R.string.difficulty_advanced)
}

@Composable fun PoseLocation.localizedLabel() = when (this) {
    PoseLocation.INDOOR -> stringResource(R.string.location_indoor)
    PoseLocation.OUTDOOR -> stringResource(R.string.location_outdoor)
    PoseLocation.STUDIO -> stringResource(R.string.location_studio)
}

@Composable fun PoseMood.localizedLabel() = when (this) {
    PoseMood.ROMANTIC -> stringResource(R.string.mood_romantic)
    PoseMood.PLAYFUL -> stringResource(R.string.mood_playful)
    PoseMood.EDITORIAL -> stringResource(R.string.mood_editorial)
    PoseMood.CINEMATIC -> stringResource(R.string.mood_cinematic)
}

@HiltViewModel
class KadrMainViewModel @Inject constructor(
    private val poseRepository: PoseRepository,
    private val shotListRepository: ShotListRepository,
    private val settingsRepository: SettingsRepository,
    private val getFilteredPosesUseCase: GetFilteredPosesUseCase
) : ViewModel() {

    val settings = settingsRepository.settingsFlow.stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), AppSettings())
    val allPoses = poseRepository.observeAllPoses().stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
    val favoritePoses = poseRepository.observeFavoritePoses().stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())
    val shotLists = shotListRepository.observeAllShotLists().stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

    val filterState = MutableStateFlow(PoseFilterState())

    @OptIn(ExperimentalCoroutinesApi::class)
    val filteredPoses = combine(filterState, settings) { f, s -> f to (s.languageTag == "ar") }
        .flatMapLatest { (f, ar) -> getFilteredPosesUseCase(f, ar) }
        .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5000), emptyList())

    fun completeOnboarding() = viewModelScope.launch { settingsRepository.setOnboardingCompleted(true) }
    fun toggleFavorite(id: String) = viewModelScope.launch { poseRepository.toggleFavorite(id) }
    fun updateQuery(q: String) = filterState.update { it.copy(query = q) }
    fun toggleSubject(s: PoseSubject?) = filterState.update { it.copy(selectedSubject = if (it.selectedSubject == s) null else s) }
    fun toggleLocation(l: PoseLocation) = filterState.update { it.copy(selectedLocation = if (it.selectedLocation == l) null else l) }
    fun toggleMood(m: PoseMood) = filterState.update { it.copy(selectedMood = if (it.selectedMood == m) null else m) }
    fun clearFilters() { filterState.value = PoseFilterState() }

    fun createList(title: String) = viewModelScope.launch { if (title.isNotBlank()) shotListRepository.createShotList(title) }
    fun deleteList(id: Long) = viewModelScope.launch { shotListRepository.deleteShotList(id) }
    fun addPoseToList(listId: Long, poseId: String) = viewModelScope.launch { shotListRepository.addPoseToShotList(listId, poseId) }
    fun toggleEntryDone(entryId: Long, done: Boolean) = viewModelScope.launch { shotListRepository.toggleEntryCompleted(entryId, done) }
    fun removeEntry(entryId: Long) = viewModelScope.launch { shotListRepository.removeEntryFromShotList(entryId) }

    fun setLanguage(tag: String) = viewModelScope.launch {
        settingsRepository.setLanguageTag(tag)
        AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags(tag))
    }
    fun setTheme(pref: ThemePreference) = viewModelScope.launch { settingsRepository.setThemePreference(pref) }
}

@Composable
fun OnboardingScreen(onComplete: () -> Unit) {
    val dimens = KadrThemeTokens.dimens
    val scope = rememberCoroutineScope()
    val titles = listOf(R.string.onboarding_title_1, R.string.onboarding_title_2, R.string.onboarding_title_3)
    val descs = listOf(R.string.onboarding_desc_1, R.string.onboarding_desc_2, R.string.onboarding_desc_3)
    val pager = rememberPagerState(pageCount = { 3 })

    Column(
        modifier = Modifier.fillMaxSize().safeDrawingPadding().padding(dimens.screenMargin),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.End) {
            TextButton(onClick = onComplete) { Text(stringResource(R.string.onboarding_skip)) }
        }
        HorizontalPager(state = pager, modifier = Modifier.weight(1f)) { page ->
            Column(
                modifier = Modifier.fillMaxSize(),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                PoseIllustrationCanvas(
                    assetName = "pose_0${page + 1}",
                    contentDesc = stringResource(titles[page]),
                    frameTint = IllustrationFrameTint.CHARCOAL_STUDIO,
                    modifier = Modifier.fillMaxWidth().height(240.dp).clip(MaterialTheme.shapes.large)
                )
                Spacer(Modifier.height(dimens.grid3))
                Text(stringResource(titles[page]), style = MaterialTheme.typography.headlineMedium, textAlign = TextAlign.Center)
                Spacer(Modifier.height(dimens.grid1))
                Text(stringResource(descs[page]), style = MaterialTheme.typography.bodyLarge, textAlign = TextAlign.Center)
            }
        }
        Button(
            onClick = {
                if (pager.currentPage < 2) scope.launch { pager.animateScrollToPage(pager.currentPage + 1) }
                else onComplete()
            },
            modifier = Modifier.fillMaxWidth().height(dimens.minTouchTarget)
        ) {
            Text(stringResource(if (pager.currentPage == 2) R.string.onboarding_start else R.string.onboarding_next))
        }
    }
}

@Composable
fun HomeScreen(
    vm: KadrMainViewModel,
    isArabic: Boolean,
    onPoseClick: (String) -> Unit,
    onSeeAllClick: () -> Unit,
    onStartShootMode: (String, Long) -> Unit,
    onSettingsClick: () -> Unit
) {
    val poses by vm.allPoses.collectAsStateWithLifecycle()
    val lists by vm.shotLists.collectAsStateWithLifecycle()
    val dimens = KadrThemeTokens.dimens

    LazyColumn(
        modifier = Modifier.fillMaxSize(),
        contentPadding = PaddingValues(dimens.screenMargin),
        verticalArrangement = Arrangement.spacedBy(dimens.grid3)
    ) {
        item {
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                Column(Modifier.weight(1f)) {
                    Text(stringResource(R.string.home_greeting), style = MaterialTheme.typography.headlineMedium)
                    Text(stringResource(R.string.home_subtitle), style = MaterialTheme.typography.bodyMedium)
                }
                IconButton(onClick = onSettingsClick) {
                    Icon(Icons.Outlined.Settings, contentDescription = stringResource(R.string.nav_settings))
                }
            }
        }
        poses.firstOrNull()?.let { featured ->
            item {
                Card(
                    onClick = { onPoseClick(featured.id) },
                    shape = MaterialTheme.shapes.large,
                    colors = CardDefaults.cardColors(containerColor = CharcoalInk)
                ) {
                    Row(Modifier.fillMaxWidth().padding(dimens.grid2), verticalAlignment = Alignment.CenterVertically) {
                        PoseIllustrationCanvas(featured.assetName, featured.localizedName(isArabic), IllustrationFrameTint.CHARCOAL_STUDIO, Modifier.size(100.dp).clip(MaterialTheme.shapes.medium))
                        Spacer(Modifier.width(dimens.grid2))
                        Column(Modifier.weight(1f)) {
                            Text(featured.localizedName(isArabic), style = MaterialTheme.typography.titleLarge, color = PureWhite)
                            Text("“${featured.localizedDirectorCue(isArabic)}”", style = MaterialTheme.typography.bodyMedium, color = PureWhite.copy(alpha = 0.85f), maxLines = 2)
                        }
                    }
                }
            }
        }
        lists.firstOrNull()?.let { activeList ->
            if (activeList.entries.isNotEmpty()) {
                item {
                    Card(shape = MaterialTheme.shapes.large, colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.secondaryContainer)) {
                        Row(Modifier.fillMaxWidth().padding(dimens.grid2), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                            Column(Modifier.weight(1f)) {
                                Text(activeList.title, style = MaterialTheme.typography.titleMedium)
                                Text(stringResource(R.string.shot_list_progress, activeList.completedCount, activeList.totalCount), style = MaterialTheme.typography.labelMedium)
                            }
                            FilledTonalButton(onClick = { onStartShootMode(activeList.entries.first().pose.id, activeList.id) }) {
                                Text(stringResource(R.string.action_enter_shoot_mode))
                            }
                        }
                    }
                }
            }
        }
        item {
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                Text(stringResource(R.string.home_trending), style = MaterialTheme.typography.titleLarge)
                TextButton(onClick = onSeeAllClick) { Text(stringResource(R.string.home_see_all)) }
            }
            LazyRow(horizontalArrangement = Arrangement.spacedBy(dimens.grid2)) {
                items(poses, key = { it.id }) { pose ->
                    PoseCard(
                        model = pose.toCardUiModel(isArabic),
                        favoriteActionContentDesc = stringResource(R.string.action_favorite_toggle),
                        onCardClick = onPoseClick,
                        onFavoriteToggle = vm::toggleFavorite,
                        modifier = Modifier.width(200.dp)
                    )
                }
            }
        }
    }
}

@Composable
fun PoseLibraryScreen(vm: KadrMainViewModel, isArabic: Boolean, onPoseClick: (String) -> Unit) {
    val poses by vm.filteredPoses.collectAsStateWithLifecycle()
    val filter by vm.filterState.collectAsStateWithLifecycle()
    val dimens = KadrThemeTokens.dimens

    Column(Modifier.fillMaxSize().padding(horizontal = dimens.screenMargin)) {
        Spacer(Modifier.height(dimens.grid2))
        OutlinedTextField(
            value = filter.query,
            onValueChange = vm::updateQuery,
            placeholder = { Text(stringResource(R.string.search_hint)) },
            leadingIcon = { Icon(Icons.Outlined.Search, null) },
            singleLine = true,
            shape = MaterialTheme.shapes.small,
            modifier = Modifier.fillMaxWidth()
        )
        Spacer(Modifier.height(dimens.grid1))
        LazyRow(horizontalArrangement = Arrangement.spacedBy(dimens.grid1)) {
            items(PoseSubject.entries) { s ->
                KadrFilterChip(s.localizedLabel(), filter.selectedSubject == s, { vm.toggleSubject(s) })
            }
            items(PoseLocation.entries) { l ->
                KadrFilterChip(l.localizedLabel(), filter.selectedLocation == l, { vm.toggleLocation(l) })
            }
            items(PoseMood.entries) { m ->
                KadrFilterChip(m.localizedLabel(), filter.selectedMood == m, { vm.toggleMood(m) })
            }
        }
        Spacer(Modifier.height(dimens.grid1))
        if (poses.isEmpty()) {
            EmptyStateView(
                title = stringResource(R.string.empty_library_title),
                subtitle = stringResource(R.string.empty_library_subtitle),
                actionLabel = stringResource(R.string.clear_filters),
                onActionClick = vm::clearFilters,
                modifier = Modifier.weight(1f)
            )
        } else {
            LazyVerticalGrid(
                columns = GridCells.Fixed(2),
                contentPadding = PaddingValues(bottom = dimens.grid4),
                horizontalArrangement = Arrangement.spacedBy(dimens.grid2),
                verticalArrangement = Arrangement.spacedBy(dimens.grid2),
                modifier = Modifier.weight(1f)
            ) {
                items(poses, key = { it.id }) { pose ->
                    PoseCard(pose.toCardUiModel(isArabic), stringResource(R.string.action_favorite_toggle), onPoseClick, vm::toggleFavorite)
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PoseDetailScreen(
    poseId: String,
    vm: KadrMainViewModel,
    isArabic: Boolean,
    onBackClick: () -> Unit,
    onEnterShootMode: (String) -> Unit
) {
    val poses by vm.allPoses.collectAsStateWithLifecycle()
    val lists by vm.shotLists.collectAsStateWithLifecycle()
    val pose = poses.firstOrNull { it.id == poseId } ?: return
    val dimens = KadrThemeTokens.dimens
    val context = LocalContext.current

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(pose.localizedName(isArabic), maxLines = 1) },
                navigationIcon = {
                    IconButton(onClick = onBackClick) { Icon(Icons.AutoMirrored.Outlined.ArrowBack, stringResource(R.string.back_button_desc)) }
                },
                actions = {
                    IconButton(onClick = {
                        val send = Intent(Intent.ACTION_SEND).apply {
                            putExtra(Intent.EXTRA_TEXT, "${pose.localizedName(isArabic)}\n${pose.localizedDirectorCue(isArabic)}")
                            type = "text/plain"
                        }
                        context.startActivity(Intent.createChooser(send, null))
                    }) { Icon(Icons.Outlined.Share, stringResource(R.string.action_share)) }
                    IconButton(onClick = { vm.toggleFavorite(pose.id) }) {
                        Icon(if (pose.isFavorite) Icons.Filled.Favorite else Icons.Outlined.FavoriteBorder, null)
                    }
                }
            )
        },
        bottomBar = {
            Surface(tonalElevation = dimens.tonalElevationMedium) {
                Row(Modifier.fillMaxWidth().navigationBarsPadding().padding(dimens.screenMargin), horizontalArrangement = Arrangement.spacedBy(dimens.grid2)) {
                    OutlinedButton(
                        onClick = { lists.firstOrNull()?.let { vm.addPoseToList(it.id, pose.id) } },
                        modifier = Modifier.weight(1f).height(dimens.minTouchTarget)
                    ) { Text(stringResource(R.string.action_add_to_list)) }
                    Button(
                        onClick = { onEnterShootMode(pose.id) },
                        modifier = Modifier.weight(1f).height(dimens.minTouchTarget)
                    ) { Text(stringResource(R.string.action_enter_shoot_mode)) }
                }
            }
        }
    ) { pad ->
        Column(
            modifier = Modifier.fillMaxSize().padding(pad).verticalScroll(rememberScrollState()).padding(dimens.screenMargin),
            verticalArrangement = Arrangement.spacedBy(dimens.grid2)
        ) {
            PoseIllustrationCanvas(pose.assetName, pose.localizedName(isArabic), IllustrationFrameTint.CHARCOAL_STUDIO, Modifier.fillMaxWidth().height(dimens.detailHeroHeight).clip(MaterialTheme.shapes.large))
            Text(pose.localizedName(isArabic), style = MaterialTheme.typography.headlineLarge)
            Text(pose.localizedDescription(isArabic), style = MaterialTheme.typography.bodyLarge)
            DirectorCueBanner(stringResource(R.string.director_cue_label), pose.localizedDirectorCue(isArabic))
            Text(stringResource(R.string.steps_section_title), style = MaterialTheme.typography.titleLarge)
            pose.localizedSteps(isArabic).forEachIndexed { idx, step ->
                Text("${idx + 1}. $step", style = MaterialTheme.typography.bodyLarge)
            }
            Card(shape = MaterialTheme.shapes.large) {
                val t = pose.photographerTips
                Column(Modifier.fillMaxWidth().padding(dimens.grid2), verticalArrangement = Arrangement.spacedBy(dimens.grid1)) {
                    Text(stringResource(R.string.tips_section_title), style = MaterialTheme.typography.titleMedium)
                    Text("${t.lensMm} • ${t.suggestedAperture} • ${t.suggestedShutter}", color = MaterialTheme.colorScheme.primary)
                    Text(if (isArabic) t.lightingAr else t.lightingEn)
                }
            }
            Text(stringResource(R.string.mistakes_section_title), style = MaterialTheme.typography.titleLarge, color = MaterialTheme.colorScheme.error)
            pose.localizedMistakes(isArabic).forEach { m -> Text("• $m") }
        }
    }
}

@Composable
fun ShootModeScreen(initialPoseId: String, vm: KadrMainViewModel, isArabic: Boolean, onExit: () -> Unit) {
    val view = LocalView.current
    DisposableEffect(view) { view.keepScreenOn = true; onDispose { view.keepScreenOn = false } }
    val poses by vm.allPoses.collectAsStateWithLifecycle()
    if (poses.isEmpty()) return
    val startIdx = poses.indexOfFirst { it.id == initialPoseId }.coerceAtLeast(0)
    val pager = rememberPagerState(initialPage = startIdx, pageCount = { poses.size })
    val dimens = KadrThemeTokens.dimens

    Column(
        modifier = Modifier.fillMaxSize().background(CharcoalInk).safeDrawingPadding().padding(dimens.screenMargin),
        verticalArrangement = Arrangement.SpaceBetween
    ) {
        Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
            TextButton(onClick = onExit) { Text(stringResource(R.string.shoot_mode_exit), color = PureWhite) }
            Text(stringResource(R.string.shoot_mode_counter, pager.currentPage + 1, poses.size), color = PureWhite)
        }
        HorizontalPager(state = pager, modifier = Modifier.weight(1f)) { page ->
            val p = poses[page]
            Column(Modifier.fillMaxSize(), horizontalAlignment = Alignment.CenterHorizontally, verticalArrangement = Arrangement.SpaceEvenly) {
                PoseIllustrationCanvas(p.assetName, p.localizedName(isArabic), IllustrationFrameTint.CHARCOAL_STUDIO, Modifier.fillMaxWidth().height(250.dp))
                Text(p.localizedName(isArabic), style = MaterialTheme.typography.headlineLarge, color = PureWhite, textAlign = TextAlign.Center)
                Text("${p.photographerTips.lensMm} • ${p.photographerTips.suggestedAperture}", color = KadrThemeTokens.colors.blushCheekAccent)
                Text("“${p.localizedDirectorCue(isArabic)}”", style = MaterialTheme.typography.headlineSmall, color = PureWhite, textAlign = TextAlign.Center)
            }
        }
    }
}

@Composable
fun ShotListScreen(vm: KadrMainViewModel, isArabic: Boolean, onPoseClick: (String) -> Unit, onStartShootMode: (String, Long) -> Unit) {
    val lists by vm.shotLists.collectAsStateWithLifecycle()
    val dimens = KadrThemeTokens.dimens
    var showDialog by remember { mutableStateOf(false) }

    Column(Modifier.fillMaxSize().padding(dimens.screenMargin)) {
        Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
            Text(stringResource(R.string.nav_shot_lists), style = MaterialTheme.typography.headlineMedium)
            Button(onClick = { showDialog = true }) { Text(stringResource(R.string.shot_list_new)) }
        }
        Spacer(Modifier.height(dimens.grid2))
        LazyColumn(verticalArrangement = Arrangement.spacedBy(dimens.grid2), modifier = Modifier.weight(1f)) {
            items(lists, key = { it.id }) { list ->
                Card(shape = MaterialTheme.shapes.large) {
                    Column(Modifier.fillMaxWidth().padding(dimens.grid2)) {
                        Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween, verticalAlignment = Alignment.CenterVertically) {
                            Text(list.title, style = MaterialTheme.typography.titleLarge, modifier = Modifier.weight(1f))
                            IconButton(onClick = { vm.deleteList(list.id) }) { Icon(Icons.Outlined.DeleteOutline, null) }
                        }
                        list.entries.forEach { entry ->
                            Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                                Checkbox(checked = entry.isCompleted, onCheckedChange = { vm.toggleEntryDone(entry.entryId, it) })
                                TextButton(onClick = { onPoseClick(entry.pose.id) }, modifier = Modifier.weight(1f)) {
                                    Text(entry.pose.localizedName(isArabic))
                                }
                                IconButton(onClick = { vm.removeEntry(entry.entryId) }) { Icon(Icons.Outlined.Close, null) }
                            }
                        }
                    }
                }
            }
        }
    }
    if (showDialog) {
        var title by remember { mutableStateOf("") }
        AlertDialog(
            onDismissRequest = { showDialog = false },
            title = { Text(stringResource(R.string.shot_list_new)) },
            text = { OutlinedTextField(value = title, onValueChange = { title = it }, singleLine = true) },
            confirmButton = {
                TextButton(onClick = { vm.createList(title); showDialog = false }) { Text(stringResource(R.string.shot_list_create)) }
            }
        )
    }
}

@Composable
fun SavedScreen(vm: KadrMainViewModel, isArabic: Boolean, onPoseClick: (String) -> Unit, onExploreClick: () -> Unit) {
    val favs by vm.favoritePoses.collectAsStateWithLifecycle()
    val dimens = KadrThemeTokens.dimens
    Column(Modifier.fillMaxSize().padding(dimens.screenMargin)) {
        Text(stringResource(R.string.nav_saved), style = MaterialTheme.typography.headlineMedium)
        Spacer(Modifier.height(dimens.grid2))
        if (favs.isEmpty()) {
            EmptyStateView(stringResource(R.string.saved_empty_title), stringResource(R.string.saved_empty_subtitle), stringResource(R.string.saved_explore_cta), onExploreClick, Modifier.weight(1f))
        } else {
            LazyVerticalGrid(columns = GridCells.Fixed(2), horizontalArrangement = Arrangement.spacedBy(dimens.grid2), verticalArrangement = Arrangement.spacedBy(dimens.grid2)) {
                items(favs, key = { it.id }) { p ->
                    PoseCard(p.toCardUiModel(isArabic), stringResource(R.string.action_favorite_toggle), onPoseClick, vm::toggleFavorite)
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingsScreen(vm: KadrMainViewModel, onBackClick: () -> Unit) {
    val settings by vm.settings.collectAsStateWithLifecycle()
    val dimens = KadrThemeTokens.dimens
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(stringResource(R.string.nav_settings)) },
                navigationIcon = { IconButton(onClick = onBackClick) { Icon(Icons.AutoMirrored.Outlined.ArrowBack, null) } }
            )
        }
    ) { pad ->
        Column(Modifier.fillMaxSize().padding(pad).padding(dimens.screenMargin), verticalArrangement = Arrangement.spacedBy(dimens.grid2)) {
            Text(stringResource(R.string.settings_language), style = MaterialTheme.typography.titleLarge)
            Row(Modifier.fillMaxWidth().selectable(settings.languageTag == "ar", onClick = { vm.setLanguage("ar") }, role = Role.RadioButton), verticalAlignment = Alignment.CenterVertically) {
                RadioButton(settings.languageTag == "ar", null)
                Spacer(Modifier.width(dimens.grid1))
                Text(stringResource(R.string.settings_lang_ar))
            }
            Row(Modifier.fillMaxWidth().selectable(settings.languageTag == "en", onClick = { vm.setLanguage("en") }, role = Role.RadioButton), verticalAlignment = Alignment.CenterVertically) {
                RadioButton(settings.languageTag == "en", null)
                Spacer(Modifier.width(dimens.grid1))
                Text(stringResource(R.string.settings_lang_en))
            }
            HorizontalDivider()
            Text(stringResource(R.string.settings_theme), style = MaterialTheme.typography.titleLarge)
            ThemePreference.entries.forEach { pref ->
                Row(Modifier.fillMaxWidth().selectable(settings.themePreference == pref, onClick = { vm.setTheme(pref) }, role = Role.RadioButton), verticalAlignment = Alignment.CenterVertically) {
                    RadioButton(settings.themePreference == pref, null)
                    Spacer(Modifier.width(dimens.grid1))
                    Text(pref.name)
                }
            }
        }
    }
}
""",

    "app/src/main/java/com/kadr/poses/MainActivity.kt": """package com.kadr.poses

import android.os.Bundle
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.BookmarkBorder
import androidx.compose.material.icons.outlined.Checklist
import androidx.compose.material.icons.outlined.GridView
import androidx.compose.material.icons.outlined.Home
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalLayoutDirection
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.LayoutDirection
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.currentBackStackEntryAsState
import androidx.navigation.compose.rememberNavController
import com.kadr.poses.domain.PoseRepository
import com.kadr.poses.domain.ThemePreference
import com.kadr.poses.ui.screens.*
import com.kadr.poses.ui.theme.KadrTheme
import dagger.hilt.android.AndroidEntryPoint
import javax.inject.Inject

@AndroidEntryPoint
class MainActivity : AppCompatActivity() {

    @Inject lateinit var poseRepository: PoseRepository

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            val vm: KadrMainViewModel = hiltViewModel()
            val settings by vm.settings.collectAsStateWithLifecycle()

            LaunchedEffect(Unit) { poseRepository.ensureSeedLoaded() }

            val isArabic = settings.languageTag == "ar"
            val dir = if (isArabic) LayoutDirection.Rtl else LayoutDirection.Ltr
            val dark = when (settings.themePreference) {
                ThemePreference.LIGHT -> false
                ThemePreference.DARK -> true
                ThemePreference.SYSTEM -> isSystemInDarkTheme()
            }

            CompositionLocalProvider(LocalLayoutDirection provides dir) {
                KadrTheme(darkTheme = dark) {
                    val nav = rememberNavController()
                    val backStack by nav.currentBackStackEntryAsState()
                    val route = backStack?.destination?.route
                    val showBar = route in listOf("home", "library", "lists", "saved")

                    Scaffold(
                        bottomBar = {
                            if (showBar) {
                                NavigationBar {
                                    NavigationBarItem(
                                        selected = route == "home",
                                        onClick = { nav.navigate("home") { launchSingleTop = true } },
                                        icon = { Icon(Icons.Outlined.Home, null) },
                                        label = { Text(stringResource(R.string.nav_home)) }
                                    )
                                    NavigationBarItem(
                                        selected = route == "library",
                                        onClick = { nav.navigate("library") { launchSingleTop = true } },
                                        icon = { Icon(Icons.Outlined.GridView, null) },
                                        label = { Text(stringResource(R.string.nav_poses)) }
                                    )
                                    NavigationBarItem(
                                        selected = route == "lists",
                                        onClick = { nav.navigate("lists") { launchSingleTop = true } },
                                        icon = { Icon(Icons.Outlined.Checklist, null) },
                                        label = { Text(stringResource(R.string.nav_shot_lists)) }
                                    )
                                    NavigationBarItem(
                                        selected = route == "saved",
                                        onClick = { nav.navigate("saved") { launchSingleTop = true } },
                                        icon = { Icon(Icons.Outlined.BookmarkBorder, null) },
                                        label = { Text(stringResource(R.string.nav_saved)) }
                                    )
                                }
                            }
                        }
                    ) { pad ->
                        NavHost(
                            navController = nav,
                            startDestination = if (settings.onboardingCompleted) "home" else "onboarding",
                            modifier = Modifier.padding(pad)
                        ) {
                            composable("onboarding") {
                                OnboardingScreen(onComplete = {
                                    vm.completeOnboarding()
                                    nav.navigate("home") { popUpTo("onboarding") { inclusive = true } }
                                })
                            }
                            composable("home") {
                                HomeScreen(
                                    vm = vm,
                                    isArabic = isArabic,
                                    onPoseClick = { nav.navigate("detail/$it") },
                                    onSeeAllClick = { nav.navigate("library") },
                                    onStartShootMode = { id, _ -> nav.navigate("shoot/$id") },
                                    onSettingsClick = { nav.navigate("settings") }
                                )
                            }
                            composable("library") {
                                PoseLibraryScreen(vm, isArabic, onPoseClick = { nav.navigate("detail/$it") })
                            }
                            composable("lists") {
                                ShotListScreen(
                                    vm = vm,
                                    isArabic = isArabic,
                                    onPoseClick = { nav.navigate("detail/$it") },
                                    onStartShootMode = { id, _ -> nav.navigate("shoot/$id") }
                                )
                            }
                            composable("saved") {
                                SavedScreen(vm, isArabic, { nav.navigate("detail/$it") }, { nav.navigate("library") })
                            }
                            composable("detail/{poseId}") { entry ->
                                val id = entry.arguments?.getString("poseId") ?: "pose_01"
                                PoseDetailScreen(id, vm, isArabic, { nav.popBackStack() }, { nav.navigate("shoot/$it") })
                            }
                            composable("shoot/{poseId}") { entry ->
                                val id = entry.arguments?.getString("poseId") ?: "pose_01"
                                ShootModeScreen(id, vm, isArabic, onExit = { nav.popBackStack() })
                            }
                            composable("settings") {
                                SettingsScreen(vm, onBackClick = { nav.popBackStack() })
                            }
                        }
                    }
                }
            }
        }
    }
}
"""
}

def main():
    for rel_path, content in FILES.items():
        full_path = PROJECT_ROOT / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content.strip() + "\n", encoding="utf-8")
    (PROJECT_ROOT / "app/src/main/assets/illustrations").mkdir(parents=True, exist_ok=True)
    print("Project files generated successfully.")

if __name__ == "__main__":
    main()
