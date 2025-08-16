WITH CallLogAgg AS (
    SELECT
        complaint_id,
        COUNT(*) AS jumlah_panggilan
    FROM
        crm_call_center_logs
    GROUP BY
        complaint_id
),

ComplaintDurations AS (
    SELECT
        complaint_id,
        product,
        "sub-product" AS sub_product,
        issue,
        submitted_via,
        EXTRACT(DAY FROM (date_sent_to_company - date_received)) AS resolution_days
    FROM
        crm_events
    WHERE
        date_sent_to_company IS NOT NULL AND date_received IS NOT NULL
)

SELECT
    cd.product,
    cd.sub_product,
    cd.issue,
    cd.submitted_via,
    COUNT(cd.complaint_id) AS total_complaints,
    ROUND(AVG(cd.resolution_days)::NUMERIC, 2) AS avg_resolution_days,
    ROUND(AVG(COALESCE(cla.jumlah_panggilan, 0))::NUMERIC, 2) AS avg_jumlah_panggilan
FROM
    ComplaintDurations cd
LEFT JOIN
    CallLogAgg cla ON cd.complaint_id = cla.complaint_id
GROUP BY
    cd.product,
    cd.sub_product,
    cd.issue,
    cd.submitted_via
ORDER BY
    avg_resolution_days DESC,
    avg_jumlah_panggilan DESC;