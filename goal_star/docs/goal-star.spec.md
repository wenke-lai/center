# Goal Star

## 項目概述

一個支援 OAuth 登入的目標管理系統，讓使用者設定目標、邀請好友監督，並在達成目標後獲得星星獎勵。

## 主要特色

OAuth 登入支援 - 支援 Google 和 GitHub 登入
目標管理 - 創建、追蹤和管理個人目標
好友監督機制 - 邀請朋友作為監督員
自動通知系統 - 目標到期時自動發送郵件給監督員
星星獎勵系統 - 完成目標獲得星星獎勵並有動畫效果

## 基本流程

使用者透過 OAuth 登入
創建新目標並設定截止日期
指定監督員的 email 和姓名
系統在截止時間自動發送通知給監督員
監督員點擊郵件連結確認目標是否達成
達成目標的使用者獲得星星獎勵
可以繼續創建新的目標

## 後端規格

### 必備條件

0. 對外提供 APIs（前端使用）以及 admin pages (管理員處理)。
1. 所有功能皆放置於 `/goal_star` app 中。
2. 所有外來鍵都放在其他 fields 下方，並且中間空一行。

### 實作細節

#### Model

`nullable = {default=None, null=True, blank=True}`
use `from django.utils.translation import gettext_lazy` for TextChoices

- Goal model

  - fields
    - name
    - description (nullable)
    - created_at
    - deadline (default=timezone.now + 30d)
    - user (FK, needs related name)
    - state
      - TextChoies: 進行中、等待驗證、完成、驗證超時
  - order by deadline

- Goal Admin page
  - do not search by user name
