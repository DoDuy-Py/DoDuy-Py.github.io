-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 12, 2022 lúc 09:26 AM
-- Phiên bản máy phục vụ: 10.4.21-MariaDB
-- Phiên bản PHP: 7.3.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `employees_manager`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `user_name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `gender` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `accounts`
--

INSERT INTO `accounts` (`id`, `user_name`, `password`, `email`, `phone`, `gender`) VALUES
(1, 'admin', '123456aA@', 'admin@gmail.com', '0987654321', 'male'),
(2, 'dovanduy', '123456', 'duy552@gmail.com', '0123456789', 'male'),
(3, 'user01', '1234a', 'user01@mail.com', '0877774651', 'female'),
(4, 'user02', '123456', 'user02@.vn', '0111111111', 'others'),
(5, 'user03', '123456', 'user03@.usa', '0934123765', 'female');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `candidate`
--

CREATE TABLE `candidate` (
  `id_can` int(11) NOT NULL,
  `name_can` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `position` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `gender` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `age` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `candidate`
--

INSERT INTO `candidate` (`id_can`, `name_can`, `position`, `email`, `phone`, `gender`, `age`) VALUES
(1, 'Nguyễn Thị Nở', 'Nhân Viên', 'thino@gmail.com', '0964661982', 'Female', 25),
(2, 'Đỗ Chí Phèo', 'Developers', 'dochipheo@gmail.com', '077777654', 'Other', 31),
(3, 'Cậu Vàng', 'Nhân Viên', 'cauvang@mail.vn', '0333333331', 'Other', 7);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `contracts`
--

CREATE TABLE `contracts` (
  `id_con` int(11) NOT NULL,
  `id_emp` int(11) NOT NULL,
  `name_con` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `name_emp` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `date_create` date NOT NULL,
  `end_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `departments`
--

CREATE TABLE `departments` (
  `id_dep` int(11) NOT NULL,
  `name_dep` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `employees`
--

CREATE TABLE `employees` (
  `id_emp` int(11) NOT NULL,
  `id_dep` int(11) NOT NULL,
  `name_emp` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `name_dep` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `gender` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `age` int(11) NOT NULL,
  `position` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `salary` int(150) NOT NULL,
  `address` varchar(150) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `employees`
--

INSERT INTO `employees` (`id_emp`, `id_dep`, `name_emp`, `name_dep`, `email`, `phone`, `gender`, `age`, `position`, `salary`, `address`) VALUES
(1, 7, 'Đỗ Văn Duy', 'Developers', 'dovanduy@gmail.com', '0987654321', 'Male', 22, 'Nhân Viên', 100000000, 'Hà Nội'),
(3, 5, 'Chí Phèo', 'Marketing', 'chipheo@gmail.com', '0123456789', 'Male', 30, 'Nhân Viên', 1000000, 'Hà Nam'),
(4, 1, 'Admin', 'CEO', 'admin@gmail.com', '0999999999', 'Female', 32, 'Giám đốc', 100000000, 'USA'),
(5, 3, 'Trạng Quỳnh', 'Tester', 'trang@gmail.com', '0111111111', 'Other', 18, 'Nhân Viên', 2000000, 'Việt Nam'),
(8, 7, 'Lê Táo', 'Developers', 'letao@mail.com', '1234567890', 'Female', 17, 'Nhân Viên', 1234567, 'TP HCM'),
(9, 3, 'Lê Bưởi', 'Marketing', 'lebuoi@mail.com', '1234565432', 'Female', 17, 'Nhân Viên', 12345678, 'TP HCM'),
(10, 3, 'Nguyễn Y Vân', 'Tester', 'nguyenvan@mail.com', '0123321123', 'Female', 24, 'Nhân Viên', 12345678, 'Hà Nội');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `candidate`
--
ALTER TABLE `candidate`
  ADD PRIMARY KEY (`id_can`);

--
-- Chỉ mục cho bảng `contracts`
--
ALTER TABLE `contracts`
  ADD PRIMARY KEY (`id_con`);

--
-- Chỉ mục cho bảng `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id_dep`);

--
-- Chỉ mục cho bảng `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id_emp`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `candidate`
--
ALTER TABLE `candidate`
  MODIFY `id_can` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `contracts`
--
ALTER TABLE `contracts`
  MODIFY `id_con` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `employees`
--
ALTER TABLE `employees`
  MODIFY `id_emp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
