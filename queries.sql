SELECT
    p.brand_name,
    p.brand_type,
    strftime('%Y', r.submission_time) as review_year,
    COUNT(r.rowid) as num_reviews,
    ROUND(AVG(r.rating), 2) as avg_rating
FROM products p
JOIN reviews r ON p.product_id = r.product_id
WHERE p.brand_type = 'influencer'
AND r.submission_time IS NOT NULL
GROUP BY p.brand_name, review_year
ORDER BY p.brand_name, review_year;